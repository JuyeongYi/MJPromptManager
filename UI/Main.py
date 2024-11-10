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
        MjPrmptBuilder.resize(848, 591)
        MjPrmptBuilder.setWindowTitle(u"MjPrmptBuilder")
        self.gridLayout = QGridLayout(MjPrmptBuilder)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.__group_pos = QGroupBox(MjPrmptBuilder)
        self.__group_pos.setObjectName(u"__group_pos")
        self.__group_pos.setMinimumSize(QSize(200, 0))
        self.lo_pos = QGridLayout(self.__group_pos)
        self.lo_pos.setObjectName(u"lo_pos")

        self.verticalLayout_2.addWidget(self.__group_pos)

        self.__group_neg = QGroupBox(MjPrmptBuilder)
        self.__group_neg.setObjectName(u"__group_neg")
        self.__group_neg.setMinimumSize(QSize(200, 0))
        self.lo_neg = QGridLayout(self.__group_neg)
        self.lo_neg.setObjectName(u"lo_neg")

        self.verticalLayout_2.addWidget(self.__group_neg)

        self.group_option = QGroupBox(MjPrmptBuilder)
        self.group_option.setObjectName(u"group_option")
        self.lo_option = QGridLayout(self.group_option)
        self.lo_option.setObjectName(u"lo_option")
        self.lo_option.setHorizontalSpacing(2)
        self.lo_option.setContentsMargins(2, 2, 2, 2)
        self.lo_option1 = QVBoxLayout()
        self.lo_option1.setObjectName(u"lo_option1")

        self.lo_option.addLayout(self.lo_option1, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.group_option)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_img = QGroupBox(MjPrmptBuilder)
        self.group_img.setObjectName(u"group_img")
        self.lo_imgInput = QVBoxLayout(self.group_img)
        self.lo_imgInput.setSpacing(2)
        self.lo_imgInput.setObjectName(u"lo_imgInput")
        self.lo_imgInput.setContentsMargins(2, 2, 2, 2)

        self.verticalLayout.addWidget(self.group_img)

        self.group_sref = QGroupBox(MjPrmptBuilder)
        self.group_sref.setObjectName(u"group_sref")
        self.lo_srefInput = QVBoxLayout(self.group_sref)
        self.lo_srefInput.setSpacing(2)
        self.lo_srefInput.setObjectName(u"lo_srefInput")
        self.lo_srefInput.setContentsMargins(2, 2, 2, 2)

        self.verticalLayout.addWidget(self.group_sref)

        self.group_cref = QGroupBox(MjPrmptBuilder)
        self.group_cref.setObjectName(u"group_cref")
        self.lo_crefInput = QVBoxLayout(self.group_cref)
        self.lo_crefInput.setObjectName(u"lo_crefInput")

        self.verticalLayout.addWidget(self.group_cref)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

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


        self.gridLayout.addLayout(self.__lo_btns, 1, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 2)
        QWidget.setTabOrder(self.textEdit, self.bt_build)
        QWidget.setTabOrder(self.bt_build, self.bt_save)
        QWidget.setTabOrder(self.bt_save, self.cb_changeSeed)

        self.retranslateUi(MjPrmptBuilder)

        QMetaObject.connectSlotsByName(MjPrmptBuilder)
    # setupUi

    def retranslateUi(self, MjPrmptBuilder):
        self.__group_pos.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Text Prompt", None))
        self.__group_neg.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Neg Prompt(-no)", None))
        self.group_option.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Options", None))
        self.group_img.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Image", None))
        self.group_sref.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Style Reference", None))
        self.group_cref.setTitle(QCoreApplication.translate("MjPrmptBuilder", u"Character Reference", None))
        self.cb_changeSeed.setText(QCoreApplication.translate("MjPrmptBuilder", u"Change Seed on Build", None))
        self.bt_save.setText(QCoreApplication.translate("MjPrmptBuilder", u"Save Prompt", None))
        self.bt_build.setText(QCoreApplication.translate("MjPrmptBuilder", u"Build Prompt", None))
        pass
    # retranslateUi

