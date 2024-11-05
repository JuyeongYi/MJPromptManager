# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FloatParm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout,
    QSizePolicy, QWidget)

class Ui_FloatParm(object):
    def setupUi(self, FloatParm):
        if not FloatParm.objectName():
            FloatParm.setObjectName(u"FloatParm")
        FloatParm.resize(292, 25)
        self.horizontalLayout = QHBoxLayout(FloatParm)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.checkBox = QCheckBox(FloatParm)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.valueWidget = QDoubleSpinBox(FloatParm)
        self.valueWidget.setObjectName(u"valueWidget")

        self.horizontalLayout.addWidget(self.valueWidget)


        self.retranslateUi(FloatParm)
        self.checkBox.toggled.connect(self.valueWidget.setEnabled)

        QMetaObject.connectSlotsByName(FloatParm)
    # setupUi

    def retranslateUi(self, FloatParm):
        FloatParm.setWindowTitle(QCoreApplication.translate("FloatParm", u"Form", None))
    # retranslateUi

