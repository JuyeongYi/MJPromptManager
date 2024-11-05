# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImgPrmpt.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_ImgInput(object):
    def setupUi(self, ImgInput):
        if not ImgInput.objectName():
            ImgInput.setObjectName(u"ImgInput")
        ImgInput.resize(338, 301)
        self.__lo_main = QGridLayout(ImgInput)
        self.__lo_main.setSpacing(2)
        self.__lo_main.setObjectName(u"__lo_main")
        self.__lo_main.setContentsMargins(2, 2, 2, 2)
        self.le_url = QLineEdit(ImgInput)
        self.le_url.setObjectName(u"le_url")

        self.__lo_main.addWidget(self.le_url, 1, 0, 1, 5)

        self.lb_img = QLabel(ImgInput)
        self.lb_img.setObjectName(u"lb_img")
        self.lb_img.setMinimumSize(QSize(320, 240))
        self.lb_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.__lo_main.addWidget(self.lb_img, 0, 0, 1, 5)

        self.btn_remove = QPushButton(ImgInput)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setMaximumSize(QSize(30, 16777215))
#if QT_CONFIG(shortcut)
        self.btn_remove.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.__lo_main.addWidget(self.btn_remove, 2, 4, 1, 1)

        self.__lb_w = QLabel(ImgInput)
        self.__lb_w.setObjectName(u"__lb_w")

        self.__lo_main.addWidget(self.__lb_w, 2, 0, 1, 1)

        self.bt_save = QPushButton(ImgInput)
        self.bt_save.setObjectName(u"bt_save")
#if QT_CONFIG(shortcut)
        self.bt_save.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.__lo_main.addWidget(self.bt_save, 2, 3, 1, 1)

        self.hsl_w = QSlider(ImgInput)
        self.hsl_w.setObjectName(u"hsl_w")
        self.hsl_w.setOrientation(Qt.Orientation.Horizontal)

        self.__lo_main.addWidget(self.hsl_w, 2, 1, 1, 1)

        self.spin_w = QDoubleSpinBox(ImgInput)
        self.spin_w.setObjectName(u"spin_w")
        self.spin_w.setMinimumSize(QSize(90, 0))
        self.spin_w.setMaximum(3.000000000000000)
        self.spin_w.setSingleStep(0.100000000000000)

        self.__lo_main.addWidget(self.spin_w, 2, 2, 1, 1)

        self.__line = QFrame(ImgInput)
        self.__line.setObjectName(u"__line")
        self.__line.setFrameShape(QFrame.Shape.HLine)
        self.__line.setFrameShadow(QFrame.Shadow.Sunken)

        self.__lo_main.addWidget(self.__line, 3, 0, 1, 5)


        self.retranslateUi(ImgInput)
        self.btn_remove.clicked.connect(ImgInput.deleteLater)

        QMetaObject.connectSlotsByName(ImgInput)
    # setupUi

    def retranslateUi(self, ImgInput):
        ImgInput.setWindowTitle(QCoreApplication.translate("ImgInput", u"Form", None))
        self.lb_img.setText(QCoreApplication.translate("ImgInput", u"img", None))
        self.btn_remove.setText(QCoreApplication.translate("ImgInput", u"X", None))
        self.__lb_w.setText(QCoreApplication.translate("ImgInput", u"Weight", None))
        self.bt_save.setText(QCoreApplication.translate("ImgInput", u"Save", None))
    # retranslateUi

