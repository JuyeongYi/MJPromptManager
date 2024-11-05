# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RefInput.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QWidget)

class Ui_RefInput(object):
    def setupUi(self, RefInput):
        if not RefInput.objectName():
            RefInput.setObjectName(u"RefInput")
        RefInput.resize(696, 138)
        self.__lo_main = QGridLayout(RefInput)
        self.__lo_main.setSpacing(2)
        self.__lo_main.setObjectName(u"__lo_main")
        self.__lo_main.setContentsMargins(2, 2, 2, 2)
        self.lb_img = QLabel(RefInput)
        self.lb_img.setObjectName(u"lb_img")
        self.lb_img.setMinimumSize(QSize(160, 120))
        self.lb_img.setMaximumSize(QSize(160, 120))
        self.lb_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.__lo_main.addWidget(self.lb_img, 0, 0, 4, 1)

        self.combo_style = QComboBox(RefInput)
        self.combo_style.addItem("")
        self.combo_style.addItem("")
        self.combo_style.setObjectName(u"combo_style")

        self.__lo_main.addWidget(self.combo_style, 0, 1, 1, 1)

        self.le_url = QLineEdit(RefInput)
        self.le_url.setObjectName(u"le_url")

        self.__lo_main.addWidget(self.le_url, 0, 2, 1, 2)

        self.__lb_w = QLabel(RefInput)
        self.__lb_w.setObjectName(u"__lb_w")

        self.__lo_main.addWidget(self.__lb_w, 1, 1, 1, 1)

        self.hsl_w = QSlider(RefInput)
        self.hsl_w.setObjectName(u"hsl_w")
        self.hsl_w.setOrientation(Qt.Orientation.Horizontal)

        self.__lo_main.addWidget(self.hsl_w, 1, 2, 1, 1)

        self.spin_w = QSpinBox(RefInput)
        self.spin_w.setObjectName(u"spin_w")
        self.spin_w.setMinimumSize(QSize(100, 0))

        self.__lo_main.addWidget(self.spin_w, 1, 3, 1, 1)

        self.bt_save = QPushButton(RefInput)
        self.bt_save.setObjectName(u"bt_save")
#if QT_CONFIG(shortcut)
        self.bt_save.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.__lo_main.addWidget(self.bt_save, 2, 3, 1, 1)

        self.bt_delete = QPushButton(RefInput)
        self.bt_delete.setObjectName(u"bt_delete")
#if QT_CONFIG(shortcut)
        self.bt_delete.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.__lo_main.addWidget(self.bt_delete, 3, 3, 1, 1)


        self.retranslateUi(RefInput)
        self.hsl_w.valueChanged.connect(self.spin_w.setValue)
        self.spin_w.valueChanged.connect(self.hsl_w.setValue)
        self.bt_delete.clicked.connect(RefInput.deleteLater)

        QMetaObject.connectSlotsByName(RefInput)
    # setupUi

    def retranslateUi(self, RefInput):
        RefInput.setWindowTitle(QCoreApplication.translate("RefInput", u"Form", None))
        self.lb_img.setText(QCoreApplication.translate("RefInput", u"img", None))
        self.combo_style.setItemText(0, QCoreApplication.translate("RefInput", u"Style", None))
        self.combo_style.setItemText(1, QCoreApplication.translate("RefInput", u"Character", None))

        self.__lb_w.setText(QCoreApplication.translate("RefInput", u"Weight", None))
        self.bt_save.setText(QCoreApplication.translate("RefInput", u"Save", None))
        self.bt_delete.setText(QCoreApplication.translate("RefInput", u"delete", None))
    # retranslateUi

