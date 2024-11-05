from UI.Main import Ui_MjPrmptBuilder
from MJPromptMaker.Widgets import *
from MJPromptMaker.GlobConst.Enums import EnumParm, ToggleParm, StrParm, NumParm

from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class MjPrmptBuilder(QtWidgets.QDialog, Ui_MjPrmptBuilder):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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

        imgInput = InputHandler(ImgInput)
        self.lo_imgInput.addWidget(imgInput)

        refInput = InputHandler(RefInput)
        self.lo_refInput.addWidget(refInput)

        self.lo_option1.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        #self.lo_option2.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        for e in EnumParm:
            enumWidget = EnumParmWidget(e)
            self.lo_option1.addWidget(enumWidget)

        for e in NumParm:
            vtype = e.type
            if vtype is int:
                numWidget = IntParmWidget(e)
                self.lo_option1.addWidget(numWidget)
                continue
            if vtype is float:
                numWidget = FloatParmWidget(e)
                self.lo_option1.addWidget(numWidget)

        for e in ToggleParm:
            toggleWidget = ToggleParmWidget(e)
            self.lo_option1.addWidget(toggleWidget)

        for e in StrParm:
            strWidget = StrParmWidget(e)
            self.lo_option1.addWidget(strWidget)

        self.bt_build.clicked.connect(self.GetPrompt)

    def GetPrompt(self):
        options = []
        for i in range(self.lo_option1.count()):
            w = self.lo_option1.itemAt(i).widget()
            wp = w.GetPrompt()
            if wp:
                options.append(wp)

        optionJoined = ' '.join(options)
        self.textEdit.setText(optionJoined)


if __name__ == '__main__':
    # show the window
    app = QtWidgets.QApplication([])

    tt = EnumParmWidget(EnumParm[0])
    print(tt.GetPrompt())

    window = MjPrmptBuilder()
    window.showMaximized()
    app.exec()
