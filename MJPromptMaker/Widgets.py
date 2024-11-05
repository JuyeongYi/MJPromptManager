from abc import abstractmethod, ABC
from enum import Enum

from PySide6 import QtWidgets, QtCore, QtGui

from MJPromptMaker.GlobConst.Enums import ToggleParm, NumParm, StrParm

from UI.InputHandler import Ui_InputHandler
from UI.ImgPrmpt import Ui_ImgInput
from UI.RefInput import Ui_RefInput
from UI.TextPrmpt import Ui_TextPrmpt

from UI.EnumParm import Ui_EnumParm
from UI.StrParm import Ui_StrParm
from UI.IntParm import Ui_IntParm
from UI.FloatParm import Ui_FloatParm
from UI.ToggleParm import Ui_ToggleParm


class MJInput(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def GetPrompt(self):
        pass


class ImgInput(MJInput, Ui_ImgInput):
    def GetPrompt(self):
        pass

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # This is defined in UI/ImgPrmpt.py file


class RefInput(MJInput, Ui_RefInput):
    def GetPrompt(self):
        pass

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # This is defined in UI/RefInput.py file


class InputHandler(QtWidgets.QWidget, Ui_InputHandler):
    def __init__(self, toInstanciate: type):
        super().__init__()
        self.setupUi(self)  # This is defined in UI/InputHandler.py file
        self.toInst = toInstanciate

        self.lo_scroll.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.bt_addNew.clicked.connect(self.AddNew)
        self.bt_clear.clicked.connect(self.ClearAll)

    def AddNew(self):
        newInput = self.toInst()
        self.lo_scroll.addWidget(newInput)

    def ClearAll(self):
        while self.lo_scroll.count():
            item = self.lo_scroll.takeAt(0)
            if item.widget():
                item.widget().deleteLater()


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
