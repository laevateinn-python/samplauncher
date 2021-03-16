# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsaZQqSh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_SetWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 496)
        MainWindow.setStyleSheet(u"background-image: url(:/ui/back_settings.png); border-radius:30px")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Montserrat Medium")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"height:42px;\n"
"width:210px;")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label.setMargin(5)

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Montserrat Medium")
        font1.setPointSize(16)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background:rgba(255,255,255,0);\n"
"color:white;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"padding:3px;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 255, 123, 100);\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius: 4px;\n"
"background-color:green;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ui/arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background:rgba(255,255,255,0);\n"
"color:white;\n"
"padding:3px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 255, 123, 100);\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius: 4px;\n"
"background-color:red;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/ui/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(-1, 2, -1, -1)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setFamily(u"Montserrat Light")
        font2.setPointSize(16)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background:rgba(249, 249, 249, 200);\n"
"color: rgba(0,0,0,200);\n"
"border-radius:10px;\n"
"border-right:0px;\n"
"}")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background: rgb(0, 85, 0);\n"
"color:white;\n"
"border-style:insect;\n"
"border-radius:5px;\n"
"padding:3px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0, 148, 109, 200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushlButton:pressed{\n"
"border-radius: 5px;\n"
"background:rgba(0, 170, 0,255);\n"
"}")
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setFont(font1)
        self.toolButton.setStyleSheet(u"QToolButton{\n"
"background:rgba(255,255,255,0);\n"
"color:white;\n"
"text-align: center;\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgba(0, 85, 0, 200);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border-radius: 4px;\n"
"background-color:green;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/ui/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QSize(24, 24))
        self.toolButton.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.toolButton, 1, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(131, 131, 131);\n"
"background:rgba(0,0,0,0);")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        font3.setPointSize(9)
        self.checkBox.setFont(font3)
        self.checkBox.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"color:rgb(88, 88, 88)")
        self.checkBox.setTristate(False)

        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamily(u"Montserrat Medium")
        font4.setPointSize(10)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:rgb(125, 125, 125)")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img height=42 width=210 src=\":/ui/logo.png\"/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043d\u0430\u0437\u0430\u0434", None))
        self.pushButton_2.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442", None))
        self.toolButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443...", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u043f\u0440\u0438 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Suvorovka launcher - ver: 1.0.0", None))
    # retranslateUi
