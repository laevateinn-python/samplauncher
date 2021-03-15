# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialoghkHPQF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(499, 298)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(499, 298))
        Dialog.setMaximumSize(QSize(499, 298))
        font = QFont()
        font.setFamily(u"Montserrat Medium")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-image: url(:/ui/back_dialog.png);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"background:rgba(255,255,255,0);\n"
"color:white;")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_closedialog = QPushButton(Dialog)
        self.pushButton_closedialog.setObjectName(u"pushButton_closedialog")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_closedialog.sizePolicy().hasHeightForWidth())
        self.pushButton_closedialog.setSizePolicy(sizePolicy1)
        self.pushButton_closedialog.setMaximumSize(QSize(20, 20))
        self.pushButton_closedialog.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_closedialog.setStyleSheet(u"background:rgba(255,255,255,0);\n"
"text-align:right;\n"
"width:6px;")
        icon = QIcon()
        icon.addFile(u":/ui/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_closedialog.setIcon(icon)
        self.pushButton_closedialog.setAutoDefault(False)
        self.pushButton_closedialog.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_closedialog)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Montserrat Medium")
        font1.setPointSize(8)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:rgba(158, 158, 158, 200);\n"
"background:rgba(255,255,255,0);\n"
"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Sunken)
        self.label_2.setLineWidth(2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u0443\u0434\u0430 \u0438\u0434\u0451\u043c \u0438\u0433\u0440\u0430\u0442\u044c?", None))
        self.pushButton_closedialog.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"*\u0414\u043b\u044f \u0442\u043e\u0433\u043e, \u0447\u0442\u043e\u0431\u044b \u0432\u0432\u043e\u0439\u0442\u0438 \u0432 \u0438\u0433\u0440\u0443, \u0432\u0430\u043c \u043d\u0430\u0434\u043e \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u0412\u043e\u0439\u0442\u0438\".", None))
    # retranslateUi

