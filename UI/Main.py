# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MjPrmptBuilder(object):
    def setupUi(self, MjPrmptBuilder):
        if not MjPrmptBuilder.objectName():
            MjPrmptBuilder.setObjectName(u"MjPrmptBuilder")
        MjPrmptBuilder.resize(878, 776)
        MjPrmptBuilder.setWindowTitle(u"MjPrmptBuilder")
        self.__lo_main = QGridLayout(MjPrmptBuilder)
        self.__lo_main.setObjectName(u"__lo_main")
        self.__group_pos = QGroupBox(MjPrmptBuilder)
        self.__group_pos.setObjectName(u"__group_pos")
        self.__group_pos.setMinimumSize(QSize(200, 0))
        self.lo_pos = QGridLayout(self.__group_pos)
        self.lo_pos.setObjectName(u"lo_pos")

        self.__lo_main.addWidget(self.__group_pos, 0, 0, 1, 1)

        self.__group_neg = QGroupBox(MjPrmptBuilder)
        self.__group_neg.setObjectName(u"__group_neg")
        self.__group_neg.setMinimumSize(QSize(200, 0))
        self.lo_neg = QGridLayout(self.__group_neg)
        self.lo_neg.setObjectName(u"lo_neg")

        self.__lo_main.addWidget(self.__group_neg, 1, 0, 1, 1)

        self.group_option = QGroupBox(MjPrmptBuilder)
        self.group_option.setObjectName(u"group_option")
        self.lo_option = QGridLayout(self.group_option)
        self.lo_option.setObjectName(u"lo_option")
        self.lo_option.setHorizontalSpacing(2)
        self.lo_option.setContentsMargins(2, 2, 2, 2)
        self.lo_option1 = QVBoxLayout()
        self.lo_option1.setObjectName(u"lo_option1")

        self.lo_option.addLayout(self.lo_option1, 0, 0, 1, 1)


        self.__lo_main.addWidget(self.group_option, 2, 0, 1, 1)

        self.__lo_btns = QGridLayout()
        self.__lo_btns.setObjectName(u"__lo_btns")
        self.cb_changeSeed = QCheckBox(MjPrmptBuilder)
        self.cb_changeSeed.setObjectName(u"cb_changeSeed")

        self.__lo_btns.addWidget(self.cb_changeSeed, 1, 1, 1, 2)

        self.bt_save = QPushButton(MjPrmptBuilder)
        self.bt_save.setObjectName(u"bt_save")

        self.__lo_btns.addWidget(self.bt_save, 0, 2, 1, 1)

        self.bt_build = QPushButton(MjPrmptBuilder)
        self.bt_build.setObjectName(u"bt_build")

        self.__lo_btns.addWidget(self.bt_build, 0, 1, 1, 1)

        self.textEdit = QTextEdit(MjPrmptBuilder)
        self.textEdit.setObjectName(u"textEdit")

        self.__lo_btns.addWidget(self.textEdit, 0, 0, 2, 1)


        self.__lo_main.addLayout(self.__lo_btns, 3, 0, 1, 3)

        self.group_img = QGroupBox(MjPrmptBuilder)
        self.group_img.setObjectName(u"group_img")
        self.lo_imgInput = QVBoxLayout(self.group_img)
        self.lo_imgInput.setSpacing(2)
        self.lo_imgInput.setObjectName(u"lo_imgInput")
        self.lo_imgInput.setContentsMargins(2, 2, 2, 2)

        self.__lo_main.addWidget(self.group_img, 0, 1, 3, 1)

        self.group_ref = QGroupBox(MjPrmptBuilder)
        self.group_ref.setObjectName(u"group_ref")
        self.lo_refInput = QVBoxLayout(self.group_ref)
        self.lo_refInput.setSpacing(2)
        self.lo_refInput.setObjectName(u"lo_refInput")
        self.lo_refInput.setContentsMargins(2, 2, 2, 2)

        self.__lo_main.addWidget(self.group_ref, 0, 2, 3, 1)


        self.retranslateUi(MjPrmptBuilder)

        QMetaObject.connectSlotsByName(MjPrmptBuilder)
    # setupUi

    def retranslateUi(self, MjPrmptBuilder):
        self.__group_pos.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Text Prompt", None))
        self.__group_neg.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Neg Prompt(-no)", None))
        self.group_option.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Options", None))
        self.cb_changeSeed.setText(QCoreApplication.translate("MjPrmptBuilder", u"Change Seed on Build", None))
        self.bt_save.setText(QCoreApplication.translate("MjPrmptBuilder", u"Save Prompt", None))
        self.bt_build.setText(QCoreApplication.translate("MjPrmptBuilder", u"Build Prompt", None))
        self.group_img.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Image", None))
        self.group_ref.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Reference", None))
        pass
    # retranslateUi

