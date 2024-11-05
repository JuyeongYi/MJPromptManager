# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StrParm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QSizePolicy, QWidget)

class Ui_StrParm(object):
    def setupUi(self, StrParm):
        if not StrParm.objectName():
            StrParm.setObjectName(u"StrParm")
        StrParm.resize(292, 25)
        self.horizontalLayout = QHBoxLayout(StrParm)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.checkBox = QCheckBox(StrParm)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.lineEdit = QLineEdit(StrParm)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(StrParm)
        self.checkBox.toggled.connect(self.lineEdit.setEnabled)

        QMetaObject.connectSlotsByName(StrParm)
    # setupUi

    def retranslateUi(self, StrParm):
        StrParm.setWindowTitle(QCoreApplication.translate("StrParm", u"Form", None))
    # retranslateUi

