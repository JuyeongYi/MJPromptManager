# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IntParm.ui'
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
    QSpinBox, QWidget)

class Ui_IntParm(object):
    def setupUi(self, IntParm):
        if not IntParm.objectName():
            IntParm.setObjectName(u"IntParm")
        IntParm.resize(292, 25)
        self.horizontalLayout = QHBoxLayout(IntParm)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.checkBox = QCheckBox(IntParm)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.valueWidget = QSpinBox(IntParm)
        self.valueWidget.setObjectName(u"valueWidget")
        self.valueWidget.setMaximum(1000000019)

        self.horizontalLayout.addWidget(self.valueWidget)


        self.retranslateUi(IntParm)
        self.checkBox.toggled.connect(self.valueWidget.setEnabled)

        QMetaObject.connectSlotsByName(IntParm)
    # setupUi

    def retranslateUi(self, IntParm):
        IntParm.setWindowTitle(QCoreApplication.translate("IntParm", u"Form", None))
    # retranslateUi

