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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_InputHandler(object):
    def setupUi(self, InputHandler):
        if not InputHandler.objectName():
            InputHandler.setObjectName(u"InputHandler")
        InputHandler.resize(298, 293)
        self.gridLayout = QGridLayout(InputHandler)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.bt_clear = QPushButton(InputHandler)
        self.bt_clear.setObjectName(u"bt_clear")
#if QT_CONFIG(shortcut)
        self.bt_clear.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.bt_clear.setFlat(False)

        self.gridLayout.addWidget(self.bt_clear, 0, 3, 1, 1)

        self.bt_addNew = QPushButton(InputHandler)
        self.bt_addNew.setObjectName(u"bt_addNew")

        self.gridLayout.addWidget(self.bt_addNew, 0, 1, 1, 1)

        self.bt_browse = QPushButton(InputHandler)
        self.bt_browse.setObjectName(u"bt_browse")
#if QT_CONFIG(shortcut)
        self.bt_browse.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.bt_browse, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.scra = QScrollArea(InputHandler)
        self.scra.setObjectName(u"scra")
        self.scra.setWidgetResizable(True)
        self.scra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrw = QWidget()
        self.scrw.setObjectName(u"scrw")
        self.scrw.setGeometry(QRect(0, 0, 292, 260))
        self.lo_scroll = QVBoxLayout(self.scrw)
        self.lo_scroll.setSpacing(2)
        self.lo_scroll.setObjectName(u"lo_scroll")
        self.lo_scroll.setContentsMargins(2, 2, 2, 2)
        self.scra.setWidget(self.scrw)

        self.gridLayout.addWidget(self.scra, 1, 0, 1, 4)


        self.retranslateUi(InputHandler)

        QMetaObject.connectSlotsByName(InputHandler)
    # setupUi

    def retranslateUi(self, InputHandler):
        InputHandler.setWindowTitle(QCoreApplication.translate("InputHandler", u"Form", None))
        self.bt_clear.setText(QCoreApplication.translate("InputHandler", u"Clear", None))
        self.bt_addNew.setText(QCoreApplication.translate("InputHandler", u"New", None))
        self.bt_browse.setText(QCoreApplication.translate("InputHandler", u"Browse", None))
    # retranslateUi

