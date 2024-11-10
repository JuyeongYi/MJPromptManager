# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TextPrmpt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QSizePolicy,
    QWidget)

from MJPromptMaker.PromptEditorWidget import PromptEditor

class Ui_TextPrmpt(object):
    def setupUi(self, TextPrmpt):
        if not TextPrmpt.objectName():
            TextPrmpt.setObjectName(u"TextPrmpt")
        TextPrmpt.resize(314, 291)
        self.gridLayout = QGridLayout(TextPrmpt)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.cb_freeze = QCheckBox(TextPrmpt)
        self.cb_freeze.setObjectName(u"cb_freeze")

        self.gridLayout.addWidget(self.cb_freeze, 1, 0, 1, 1)

        self.text_prompt = PromptEditor(TextPrmpt)
        self.text_prompt.setObjectName(u"text_prompt")

        self.gridLayout.addWidget(self.text_prompt, 0, 0, 1, 2)


        self.retranslateUi(TextPrmpt)
        self.cb_freeze.clicked["bool"].connect(self.text_prompt.setDisabled)

        QMetaObject.connectSlotsByName(TextPrmpt)
    # setupUi

    def retranslateUi(self, TextPrmpt):
        TextPrmpt.setWindowTitle(QCoreApplication.translate("TextPrmpt", u"Form", None))
        self.cb_freeze.setText(QCoreApplication.translate("TextPrmpt", u"Freeze", None))
    # retranslateUi

