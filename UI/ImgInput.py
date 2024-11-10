# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImgInput.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QWidget)

class Ui_ImgInput(object):
    def setupUi(self, ImgInput):
        if not ImgInput.objectName():
            ImgInput.setObjectName(u"ImgInput")
        ImgInput.resize(810, 338)
        self.gridLayout_2 = QGridLayout(ImgInput)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.lb_img = QLabel(ImgInput)
        self.lb_img.setObjectName(u"lb_img")
        self.lb_img.setMinimumSize(QSize(256, 0))
        self.lb_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_img, 0, 0, 1, 1)

        self.lo_grid = QGridLayout()
        self.lo_grid.setObjectName(u"lo_grid")
        self.hsl_w = QSlider(ImgInput)
        self.hsl_w.setObjectName(u"hsl_w")
        self.hsl_w.setMaximum(10)
        self.hsl_w.setValue(1)
        self.hsl_w.setOrientation(Qt.Orientation.Horizontal)

        self.lo_grid.addWidget(self.hsl_w, 1, 1, 1, 1)

        self.lb_label = QLabel(ImgInput)
        self.lb_label.setObjectName(u"lb_label")

        self.lo_grid.addWidget(self.lb_label, 2, 0, 1, 1)

        self.spin_w = QSpinBox(ImgInput)
        self.spin_w.setObjectName(u"spin_w")
        self.spin_w.setMinimumSize(QSize(100, 0))
        self.spin_w.setMaximum(10)
        self.spin_w.setValue(1)

        self.lo_grid.addWidget(self.spin_w, 1, 2, 1, 1)

        self.bt_delete = QPushButton(ImgInput)
        self.bt_delete.setObjectName(u"bt_delete")
#if QT_CONFIG(shortcut)
        self.bt_delete.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.lo_grid.addWidget(self.bt_delete, 3, 2, 1, 1)

        self.le_tag = QLineEdit(ImgInput)
        self.le_tag.setObjectName(u"le_tag")

        self.lo_grid.addWidget(self.le_tag, 3, 1, 1, 1)

        self.__lb_url = QLabel(ImgInput)
        self.__lb_url.setObjectName(u"__lb_url")

        self.lo_grid.addWidget(self.__lb_url, 0, 0, 1, 1)

        self.le_url = QLineEdit(ImgInput)
        self.le_url.setObjectName(u"le_url")

        self.lo_grid.addWidget(self.le_url, 0, 1, 1, 2)

        self.__lb_tag = QLabel(ImgInput)
        self.__lb_tag.setObjectName(u"__lb_tag")

        self.lo_grid.addWidget(self.__lb_tag, 3, 0, 1, 1)

        self.le_label = QLineEdit(ImgInput)
        self.le_label.setObjectName(u"le_label")

        self.lo_grid.addWidget(self.le_label, 2, 1, 1, 1)

        self.__lb_w = QLabel(ImgInput)
        self.__lb_w.setObjectName(u"__lb_w")

        self.lo_grid.addWidget(self.__lb_w, 1, 0, 1, 1)

        self.bt_save = QPushButton(ImgInput)
        self.bt_save.setObjectName(u"bt_save")
#if QT_CONFIG(shortcut)
        self.bt_save.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.lo_grid.addWidget(self.bt_save, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.lo_grid, 0, 1, 1, 1)

        QWidget.setTabOrder(self.le_url, self.hsl_w)
        QWidget.setTabOrder(self.hsl_w, self.spin_w)

        self.retranslateUi(ImgInput)
        self.hsl_w.valueChanged.connect(self.spin_w.setValue)
        self.spin_w.valueChanged.connect(self.hsl_w.setValue)
        self.bt_delete.clicked.connect(ImgInput.deleteLater)

        QMetaObject.connectSlotsByName(ImgInput)
    # setupUi

    def retranslateUi(self, ImgInput):
        ImgInput.setWindowTitle(QCoreApplication.translate("ImgInput", u"Form", None))
        self.lb_img.setText(QCoreApplication.translate("ImgInput", u"img", None))
        self.lb_label.setText(QCoreApplication.translate("ImgInput", u"Label", None))
        self.bt_delete.setText(QCoreApplication.translate("ImgInput", u"delete", None))
        self.__lb_url.setText(QCoreApplication.translate("ImgInput", u"URL", None))
        self.__lb_tag.setText(QCoreApplication.translate("ImgInput", u"Tags", None))
        self.__lb_w.setText(QCoreApplication.translate("ImgInput", u"Weight", None))
        self.bt_save.setText(QCoreApplication.translate("ImgInput", u"Save", None))
    # retranslateUi

