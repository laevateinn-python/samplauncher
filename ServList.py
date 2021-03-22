# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYSpbCu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc


class Ui_ServList(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(226, 81)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet(u"background:rgba(255,255,255,255);\n"
"border-radius: 20px;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.indicator = QLabel(Form)
        self.indicator.setObjectName(u"indicator")
        sizePolicy.setHeightForWidth(self.indicator.sizePolicy().hasHeightForWidth())
        self.indicator.setSizePolicy(sizePolicy)
        self.indicator.setPixmap(QPixmap(":/ui/red_led.png").scaledToWidth(21))
        self.indicator.setStyleSheet(u"QLabel{\n"
"background: rgba(0,0,0,0); margin-right:5px;\n"
"}")

        self.horizontalLayout.addWidget(self.indicator)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.servername_label = QLabel(Form)
        self.servername_label.setObjectName(u"servername_label")
        sizePolicy.setHeightForWidth(self.servername_label.sizePolicy().hasHeightForWidth())
        self.servername_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Montserrat Medium")
        font.setPointSize(14)
        self.servername_label.setFont(font)
        self.servername_label.setStyleSheet(u"QLabel{\n"
"background: rgba(0,0,0,0);\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.servername_label)

        self.online_label = QLabel(Form)
        self.online_label.setObjectName(u"online_label")
        sizePolicy.setHeightForWidth(self.online_label.sizePolicy().hasHeightForWidth())
        self.online_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Montserrat Medium")
        font1.setPointSize(9)
        self.online_label.setFont(font1)
        self.online_label.setStyleSheet(u"QLabel{\n"
"background: rgba(0,0,0,0);\n"
"color:white;\n"
"}")

        self.verticalLayout.addWidget(self.online_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.indicator.setText("")
        self.servername_label.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0432\u0438\u0439 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.online_label.setText(QCoreApplication.translate("Form", u"\u041e\u043d\u043b\u0430\u0439\u043d: 100 \u0438\u0437 1000", None))
    # retranslateUi
