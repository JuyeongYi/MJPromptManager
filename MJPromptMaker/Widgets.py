from abc import abstractmethod
from dataclasses import dataclass, replace
from typing import Optional

from PySide6 import QtWidgets, QtCore, QtGui

from MJPromptMaker.GlobConst import ToggleParm, NumParm, StrParm, ImageInputType
from MJPromptMaker.ImageHandler import ImageInfo
from UI.EnumParm import Ui_EnumParm
from UI.FloatParm import Ui_FloatParm
from UI.ImgInput import Ui_ImgInput
from UI.InputHandler import Ui_InputHandler
from UI.IntParm import Ui_IntParm
from UI.StrParm import Ui_StrParm
from UI.TextPrmpt import Ui_TextPrmpt
from UI.ToggleParm import Ui_ToggleParm


class MJInput(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def GetPrompt(self):
        pass


class ImgInput(MJInput, Ui_ImgInput):

    def __init__(self, imageDownloader, imgType):
        super().__init__()
        self.setupUi(self)  # This is defined in UI/ImgPrmpt.py file
        self.imageDownloader = imageDownloader
        self.imgType = imgType
        self.imgInfo: Optional[ImageInfo] = None
        self.le_url.editingFinished.connect(self.SetImageInfoByURL)
        self.lo_grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.bt_save.clicked.connect(self.Rename)

    def Rename(self):
        self.imgInfo.tags = tuple(map(str.strip, self.le_tag.text().split(',')))
        self.imgInfo = self.imgInfo.Rename(self.le_label.text())

    def GetPrompt(self):
        weight = self.spin_w.value()
        url = self.imgInfo.url if self.imgInfo is not None else self.le_url.text()
        if url.isnumeric() or self.imgInfo is not None:
            if weight == 1:
                return f"{url}"
            else:
                return f"{url}::{weight}"

        else:
            return ""

    def SetImageInfoByURL(self):
        url = self.le_url.text()
        isNumeric = url.isnumeric()
        if isNumeric and self.imgType != ImageInputType.sw:
            QtWidgets.QMessageBox.warning(self, "Image Input Warning", "Only Style Reference can be numeric.")
            return

        images = tuple(self.imageDownloader.SaveDir.glob(f"{url}.json"))
        imgInfo = None
        if images:
            imgInfo = ImageInfo.FromJSON(images[0])

        else:
            if isNumeric:
                self.lb_img.setText("integer seed input\n(premaid image not exists)")
                self.le_label.setText(imgInfo)
                return
            else:
                imgInfo = self.imageDownloader.DownloadImage(url)

        if imgInfo is None:
            return
        self.imgInfo = imgInfo
        self.le_label.setText(imgInfo.filename.stem)
        self.le_tag.setText(', '.join(imgInfo.tags))
        pixmap = QtGui.QPixmap(str(imgInfo.filename))
        self.lb_img.setPixmap(pixmap.scaled(256, 256, QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                            QtCore.Qt.TransformationMode.SmoothTransformation))


class InputHandler(MJInput, QtWidgets.QWidget, Ui_InputHandler):
    def __init__(self, imgType: ImageInputType, imageDownloader):
        super().__init__()
        self.setupUi(self)
        self.imageDownloader = imageDownloader
        self.imgType = imgType

        if imgType.value.t is float:
            lb = QtWidgets.QLabel(imgType.name)
            self.lo_weight.addWidget(lb)

            slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
            slider.setMinimum(imgType.value.minValue)
            slider.setMaximum(imgType.value.maxValue * 100)
            slider.setValue(imgType.value.defaultValue * 100)
            self.lo_weight.addWidget(slider)

            valueLb = QtWidgets.QLabel(f"{imgType.value.defaultValue:.2f}")
            self.lo_weight.addWidget(valueLb)
            slider.valueChanged.connect(lambda: valueLb.setText(f"{slider.value() / 100:.2f}"))
            self.lb_weightValue = valueLb

            pass
        elif imgType.value.t is int:
            lb = QtWidgets.QLabel(imgType.name)
            self.lo_weight.addWidget(lb)

            slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
            slider.setMinimum(imgType.value.minValue)
            slider.setMaximum(imgType.value.maxValue)
            slider.setValue(imgType.value.defaultValue)
            self.lo_weight.addWidget(slider)

            valueLb = QtWidgets.QLabel(str(imgType.value.defaultValue))
            self.lo_weight.addWidget(valueLb)
            slider.valueChanged.connect(lambda: valueLb.setText(str(slider.value())))
            self.lb_weightValue = valueLb

        self.lo_scroll.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.bt_addNew.clicked.connect(self.AddNew)
        self.bt_clear.clicked.connect(self.ClearAll)

    def AddNew(self):
        newInput = ImgInput(self.imageDownloader, self.imgType)
        self.lo_scroll.addWidget(newInput)

    def ClearAll(self):
        while self.lo_scroll.count():
            item = self.lo_scroll.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def GetWeight(self):
        wCount = self.lo_scroll.count()
        if wCount > 0:
            toReturn = f"--{self.imgType.name} {self.lb_weightValue.text()} "
            return toReturn
        return ""

    def GetPrompt(self):
        wCount = self.lo_scroll.count()

        if wCount > 0:
            if self.imgType == ImageInputType.iw:
                if wCount < 2:
                    QtWidgets.QMessageBox.warning(self, "Image Input Warning",
                                                  "Image input: at least 2 images are required.")

            promptList = []

            for i in range(wCount):
                w = self.lo_scroll.itemAt(i).widget()
                prompt = w.GetPrompt()
                promptList.append(prompt)

            return f"{self.imgType.value.prefix} {' '.join(promptList)}"
        return ""


class TextPrmpt(MJInput, Ui_TextPrmpt):

    def __init__(self, paramName: str = ""):
        super().__init__()
        self.setupUi(self)
        self.param = paramName

    def GetPrompt(self):
        text = self.text_prompt.toPlainText()

        pass


class StrParmWidget(MJInput, Ui_StrParm):
    def GetPrompt(self):
        if self.checkBox.isChecked():
            return self.enum(self.lineEdit.text())
        return ""

    def __init__(self, parmEnum: StrParm):
        super().__init__()
        self.setupUi(self)
        self.enum = parmEnum
        self.checkBox.setText(self.enum.name)


class EnumParmWidget(MJInput, Ui_EnumParm):
    def GetPrompt(self):
        if self.checkBox.isChecked():
            return self.enum[self.comboBox.currentText()]()
        return ""

    def __init__(self, parmEnum: type):
        super().__init__()
        self.setupUi(self)
        self.enum = parmEnum
        self.checkBox.setText(self.enum.__name__)
        for e in self.enum:
            self.comboBox.addItem(e.name)


class ToggleParmWidget(MJInput, Ui_ToggleParm):
    def GetPrompt(self):
        return self.toggle() if self.checkBox.isChecked() else ""

    def __init__(self, parmEnum: ToggleParm):
        super().__init__()
        self.setupUi(self)
        self.toggle = parmEnum
        self.checkBox.setText(self.toggle.name)


class IntParmWidget(MJInput, Ui_IntParm):
    def GetPrompt(self):
        if self.checkBox.isChecked():
            return f"--{self.checkBox.text()} {self.valueWidget.value()}"
        else:
            return ""

    def __init__(self, e: NumParm):
        super().__init__()
        self.setupUi(self)
        self.checkBox.setText(e.name)
        self.valueWidget.setMinimum(e.min)
        self.valueWidget.setMaximum(e.max)
        self.valueWidget.setValue(e.default)
        self.valueWidget.setSingleStep(max(1, int(e.max / 100.0)))


class FloatParmWidget(MJInput, Ui_FloatParm):
    def GetPrompt(self):
        if self.checkBox.isChecked():
            return f"--{self.checkBox.text()} {self.valueWidget.value()}"
        else:
            return ""

    def __init__(self, e: NumParm):
        super().__init__()
        self.setupUi(self)
        self.checkBox.setText(e.name)
        self.valueWidget.setMinimum(e.min)
        self.valueWidget.setMaximum(e.max)
        self.valueWidget.setValue(e.default)
        self.valueWidget.setSingleStep(e.max / 100.0)
