# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EnumParm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QSizePolicy, QWidget)

class Ui_EnumParm(object):
    def setupUi(self, EnumParm):
        if not EnumParm.objectName():
            EnumParm.setObjectName(u"EnumParm")
        EnumParm.resize(221, 25)
        self.__lo = QHBoxLayout(EnumParm)
        self.__lo.setSpacing(1)
        self.__lo.setObjectName(u"__lo")
        self.__lo.setContentsMargins(1, 1, 1, 1)
        self.checkBox = QCheckBox(EnumParm)
        self.checkBox.setObjectName(u"checkBox")

        self.__lo.addWidget(self.checkBox)

        self.comboBox = QComboBox(EnumParm)
        self.comboBox.setObjectName(u"comboBox")

        self.__lo.addWidget(self.comboBox)


        self.retranslateUi(EnumParm)
        self.checkBox.toggled.connect(self.comboBox.setEnabled)

        QMetaObject.connectSlotsByName(EnumParm)
    # setupUi

    def retranslateUi(self, EnumParm):
        pass
    # retranslateUi

