# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputHandler.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_InputHandler(object):
    def setupUi(self, InputHandler):
        if not InputHandler.objectName():
            InputHandler.setObjectName(u"InputHandler")
        InputHandler.resize(302, 140)
        self.lo_main = QVBoxLayout(InputHandler)
        self.lo_main.setObjectName(u"lo_main")
        self.__lo_btns = QHBoxLayout()
        self.__lo_btns.setObjectName(u"__lo_btns")
        self.lo_weight = QHBoxLayout()
        self.lo_weight.setObjectName(u"lo_weight")

        self.__lo_btns.addLayout(self.lo_weight)

        self.bt_addNew = QPushButton(InputHandler)
        self.bt_addNew.setObjectName(u"bt_addNew")
        self.bt_addNew.setMaximumSize(QSize(100, 16777215))

        self.__lo_btns.addWidget(self.bt_addNew)

        self.bt_browse = QPushButton(InputHandler)
        self.bt_browse.setObjectName(u"bt_browse")
        self.bt_browse.setMaximumSize(QSize(100, 16777215))
#if QT_CONFIG(shortcut)
        self.bt_browse.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.__lo_btns.addWidget(self.bt_browse)

        self.bt_clear = QPushButton(InputHandler)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setMaximumSize(QSize(100, 16777215))
#if QT_CONFIG(shortcut)
        self.bt_clear.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.bt_clear.setFlat(False)

        self.__lo_btns.addWidget(self.bt_clear)


        self.lo_main.addLayout(self.__lo_btns)

        self.scra = QScrollArea(InputHandler)
        self.scra.setObjectName(u"scra")
        self.scra.setWidgetResizable(True)
        self.scra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrw = QWidget()
        self.scrw.setObjectName(u"scrw")
        self.scrw.setGeometry(QRect(0, 0, 282, 87))
        self.lo_scroll = QVBoxLayout(self.scrw)
        self.lo_scroll.setSpacing(2)
        self.lo_scroll.setObjectName(u"lo_scroll")
        self.lo_scroll.setContentsMargins(2, 2, 2, 2)
        self.scra.setWidget(self.scrw)

        self.lo_main.addWidget(self.scra)

        QWidget.setTabOrder(self.bt_addNew, self.bt_browse)
        QWidget.setTabOrder(self.bt_browse, self.bt_clear)
        QWidget.setTabOrder(self.bt_clear, self.scra)

        self.retranslateUi(InputHandler)

        QMetaObject.connectSlotsByName(InputHandler)
    # setupUi

    def retranslateUi(self, InputHandler):
        InputHandler.setWindowTitle(QCoreApplication.translate("InputHandler", u"Form", None))
        self.bt_addNew.setText(QCoreApplication.translate("InputHandler", u"New", None))
        self.bt_browse.setText(QCoreApplication.translate("InputHandler", u"Browse", None))
        self.bt_clear.setText(QCoreApplication.translate("InputHandler", u"Clear", None))
    # retranslateUi

