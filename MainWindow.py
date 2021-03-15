# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledOYgBvT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 496)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(978, 496))
        MainWindow.setMaximumSize(QSize(978, 496))
        font = QFont()
        font.setFamily(u"Segoe UI Symbol")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-image: url(:/ui/back_colored.png);\n"
"")
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(16)
        self.centralwidget.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(28, 3, 28, 11)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(10, 3, -1, -1)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setStyleSheet(u"background:rgba(255,255,255,0);\n"
"height:210px;\n"
"width:40px;\n"
"")
        self.logo.setTextFormat(Qt.AutoText)
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.logo.setWordWrap(False)
        self.logo.setMargin(5)

        self.horizontalLayout.addWidget(self.logo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_site = QPushButton(self.centralwidget)
        self.pushButton_site.setObjectName(u"pushButton_site")
        font2 = QFont()
        font2.setFamily(u"Montserrat Medium")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_site.setFont(font2)
        self.pushButton_site.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_site.setStyleSheet(u"background:rgba(255,255,255,10);\n"
"color:white;\n"
"margin-bottom:12px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"")
        self.pushButton_site.setAutoDefault(False)
        self.pushButton_site.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_site)

        self.pushButton_forum = QPushButton(self.centralwidget)
        self.pushButton_forum.setObjectName(u"pushButton_forum")
        self.pushButton_forum.setFont(font1)
        self.pushButton_forum.setStyleSheet(u"background:rgba(255,255,255,10);\n"
"color:white;\n"
"margin-bottom:12px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"")
        self.pushButton_forum.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_forum)

        self.pushButton_commun = QPushButton(self.centralwidget)
        self.pushButton_commun.setObjectName(u"pushButton_commun")
        self.pushButton_commun.setFont(font1)
        self.pushButton_commun.setStyleSheet(u"color:white;\n"
"background:rgba(255,255,255,10);\n"
"margin-bottom:12px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"")
        self.pushButton_commun.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_commun)

        self.pushButton_shop = QPushButton(self.centralwidget)
        self.pushButton_shop.setObjectName(u"pushButton_shop")
        self.pushButton_shop.setFont(font1)
        self.pushButton_shop.setStyleSheet(u"color:white;\n"
"background:rgba(255,255,255,10);\n"
"margin-bottom:12px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"")
        self.pushButton_shop.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_shop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_set = QPushButton(self.centralwidget)
        self.pushButton_set.setObjectName(u"pushButton_set")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_set.sizePolicy().hasHeightForWidth())
        self.pushButton_set.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        font3.setPointSize(10)
        self.pushButton_set.setFont(font3)
        self.pushButton_set.setStyleSheet(u"background:rgba(255,255,255,10);")
        icon = QIcon()
        icon.addFile(u":/ui/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set.setIcon(icon)
        self.pushButton_set.setIconSize(QSize(16, 16))
        self.pushButton_set.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_set)

        self.pushButton_minim = QPushButton(self.centralwidget)
        self.pushButton_minim.setObjectName(u"pushButton_minim")
        sizePolicy1.setHeightForWidth(self.pushButton_minim.sizePolicy().hasHeightForWidth())
        self.pushButton_minim.setSizePolicy(sizePolicy1)
        self.pushButton_minim.setStyleSheet(u"background:rgba(255,255,255,10);")
        icon1 = QIcon()
        icon1.addFile(u":/ui/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minim.setIcon(icon1)
        self.pushButton_minim.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_minim)

        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy1.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy1)
        self.pushButton_close.setStyleSheet(u"background:rgba(255,255,255,10);")
        icon2 = QIcon()
        icon2.addFile(u":/ui/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_close)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_serv = QVBoxLayout()
        self.verticalLayout_serv.setObjectName(u"verticalLayout_serv")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Montserrat Medium")
        font4.setPointSize(26)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color:white;\n"
"background:rgba(255,255,255,0);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_serv.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.listView_servers = QListView(self.centralwidget)
        self.listView_servers.setObjectName(u"listView_servers")
        self.listView_servers.setStyleSheet(u"background:rgba(255,255,255,0);")
        self.listView_servers.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_3.addWidget(self.listView_servers)


        self.verticalLayout_serv.addLayout(self.horizontalLayout_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamily(u"Montserrat SemiBold")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"background:rgba(255,255,255,0);\n"
"color:white;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_serv.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_serv)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color:white;\n"
"background:rgba(255,255,255,0);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listView_news = QListView(self.centralwidget)
        self.listView_news.setObjectName(u"listView_news")
        self.listView_news.setStyleSheet(u"background:rgba(255,255,255,0);\n"
"")
        self.listView_news.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_4.addWidget(self.listView_news)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_load2 = QLabel(self.centralwidget)
        self.label_load2.setObjectName(u"label_load2")
        font6 = QFont()
        font6.setFamily(u"Montserrat ExtraBold")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_load2.setFont(font6)
        self.label_load2.setStyleSheet(u"color:white;\n"
"background:rgba(255,255,255,0);")
        self.label_load2.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.label_load2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font6)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"border-radius: 10px;\n"
"text-align:left;\n"
"background:rgba(143, 143, 143,50);\n"
"color:white;")
        self.progressBar.setValue(29)
        self.progressBar.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.label_load = QLabel(self.centralwidget)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setFont(font6)
        self.label_load.setStyleSheet(u"color:white;\n"
"background:rgba(255,255,255,0);")

        self.verticalLayout_4.addWidget(self.label_load)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setBaseSize(QSize(0, 0))
        self.lineEdit.setFont(font6)
        self.lineEdit.setStyleSheet(u"color:rgb(134, 134, 134);\n"
"height:30px;\n"
"width:220px;\n"
"border-radius: 7px;\n"
"text-align:center;\n"
"background:rgba(143, 143, 143,50);\n"
"")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setFrame(False)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton_play = QPushButton(self.centralwidget)
        self.pushButton_play.setObjectName(u"pushButton_play")
        self.pushButton_play.setAutoFillBackground(False)
        self.pushButton_play.setStyleSheet(u"background:rgba(255,255,255,0);")
        icon3 = QIcon()
        icon3.addFile(u":/ui/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_play.setIcon(icon3)
        self.pushButton_play.setIconSize(QSize(200, 100))
        self.pushButton_play.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton_play)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close)
        self.pushButton_minim.clicked.connect(MainWindow.showMinimized)

        self.pushButton_site.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img height=42 width=210 src=\":/ui/logo.png\"/></p></body></html>", None))
        self.pushButton_site.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u0439\u0442", None))
        self.pushButton_forum.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u0443\u043c", None))
        self.pushButton_commun.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u043e", None))
        self.pushButton_shop.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.pushButton_set.setText("")
        self.pushButton_minim.setText("")
        self.pushButton_close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0448\u0438 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0439 \u043e\u043d\u043b\u0430\u0439\u043d: 10", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438 \u041f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.label_load2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0438\u043e\u0442 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.label_load.setText(QCoreApplication.translate("MainWindow", u"C:\\userotsosi", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.pushButton_play.setText("")
    # retranslateUi

