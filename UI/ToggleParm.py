# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToggleParm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QSizePolicy,
    QWidget)

class Ui_ToggleParm(object):
    def setupUi(self, ToggleParm):
        if not ToggleParm.objectName():
            ToggleParm.setObjectName(u"ToggleParm")
        ToggleParm.resize(292, 25)
        self.horizontalLayout = QHBoxLayout(ToggleParm)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.checkBox = QCheckBox(ToggleParm)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.retranslateUi(ToggleParm)

        QMetaObject.connectSlotsByName(ToggleParm)
    # setupUi

    def retranslateUi(self, ToggleParm):
        ToggleParm.setWindowTitle(QCoreApplication.translate("ToggleParm", u"Form", None))
    # retranslateUi

