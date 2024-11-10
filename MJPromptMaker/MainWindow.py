from typing import Dict

from UI.Main import Ui_MjPrmptBuilder
from MJPromptMaker.Widgets import *
from MJPromptMaker.GlobConst import EnumParm, ToggleParm, StrParm, NumParm, ImageInputType
from MJPromptMaker.ImageHandler import ImageDownloader

from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class MjPrmptBuilder(QtWidgets.QDialog, Ui_MjPrmptBuilder):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.imageDownloader = ImageDownloader("image")

        self.setWindowFlags(
            Qt.WindowType.Dialog |
            Qt.WindowType.WindowMinimizeButtonHint |  # 최소화 버튼
            Qt.WindowType.WindowMaximizeButtonHint |  # 최대화 버튼
            Qt.WindowType.WindowCloseButtonHint  # 닫기 버튼
        )

        self.posPrompt = TextPrmpt()
        self.lo_pos.addWidget(self.posPrompt)

        self.negPrompt = TextPrmpt()
        self.lo_neg.addWidget(self.negPrompt)

        imgLos = (self.lo_imgInput, self.lo_srefInput, self.lo_crefInput)
        self.imgHandlers: Dict[ImageInputType, InputHandler] = dict()

        for imgLo, imgType in zip(imgLos, ImageInputType):
            imgInput = InputHandler(imgType, self.imageDownloader)
            self.imgHandlers[imgType] = imgInput
            imgLo.addWidget(imgInput)

        self.lo_option1.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        # self.lo_option2.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        for e in EnumParm:
            enumWidget = EnumParmWidget(e)
            enumWidget.comboBox.setEnabled(False)
            self.lo_option1.addWidget(enumWidget)

        for e in NumParm:
            vtype = e.type
            if vtype is int:
                numWidget = IntParmWidget(e)
                numWidget.valueWidget.setEnabled(False)
                self.lo_option1.addWidget(numWidget)
                continue
            if vtype is float:
                numWidget = FloatParmWidget(e)
                numWidget.valueWidget.setEnabled(False)
                self.lo_option1.addWidget(numWidget)

        for e in ToggleParm:
            toggleWidget = ToggleParmWidget(e)
            self.lo_option1.addWidget(toggleWidget)

        for e in StrParm:
            strWidget = StrParmWidget(e)
            strWidget.lineEdit.setEnabled(False)
            self.lo_option1.addWidget(strWidget)

        self.bt_build.clicked.connect(self.GetPrompt)

    def GetPrompt(self):

        imgInW = {e: self.imgHandlers[e].GetWeight() for e in ImageInputType}
        imgInPrmpt = {e: self.imgHandlers[e].GetPrompt() for e in ImageInputType}

        imgInputPrompt = imgInPrmpt[ImageInputType.iw]

        posTextPrompt = self.posPrompt.text_prompt.toPlainText()

        negText = self.negPrompt.text_prompt.toPlainText()
        negTextPrompt = f"--no {negText}" if len(negText) > 0 else ""

        options = [imgInW[ImageInputType.iw]]
        for i in range(self.lo_option1.count()):
            w = self.lo_option1.itemAt(i).widget()
            wp = w.GetPrompt()
            if wp:
                options.append(wp)

        for e in (ImageInputType.sw, ImageInputType.cw):
            options.append(f"{imgInW[e]}{imgInPrmpt[e]}")
        optionJoined = ' '.join(options)

        prompt = f"/imagine prompt:{imgInputPrompt} {posTextPrompt} {negTextPrompt} {optionJoined}"
        self.textEdit.setText(prompt)
