
import sys
import os
import webbrowser
import json
import time

from SAMP_model import *
import re
from pathlib import Path
import winreg
from threading import Thread

from PySide2.QtWidgets import *
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap, QFont
from MainWindow import Ui_MainWindow
from SettingsUi import Ui_SetWindow
from ServDialog import Ui_Dialog
from ServList import Ui_ServList
import subprocess


BASE_DIR = Path(__file__).resolve().parent

class Launcher(QMainWindow):
    def __init__(self, confPath,parent=None):
        super(Launcher, self).__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
   
# VA    
        self.config = Config().getConfigObj()

        

# set up UI
        self.set_ui = SettingsUi()
        
        setLauncher(self.set_ui, confPath)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.serverlistwidget = serverListWidget()
        self.ui.horizontalLayout_3.addWidget(self.serverlistwidget)
        self.ui.lineEdit.setText(self.config.get_val("Web",'username'))
       

    

#signals
        self.ui.pushButton_set.clicked.connect(self.set_ui.show)
        self.ui.pushButton_site.clicked.connect(lambda: webbrowser.open("http://suvorovka-rp.ru"))
        self.ui.pushButton_forum.clicked.connect(lambda: webbrowser.open("http://forum.suvorovka-rp.ru"))
        self.ui.pushButton_commun.clicked.connect(lambda: webbrowser.open("https://vk.com/suvorovka.crmp"))
        self.ui.pushButton_shop.clicked.connect(lambda: webbrowser.open("http://shop.suvorovka-rp.ru"))
        self.ui.pushButton_play.clicked.connect(lambda: self.play(self.config))
        self.ui.lineEdit.textEdited.connect(lambda: self.changeUserName())
    def play(self,config):

        directory = config.get_val("Settings","pathclient")
        address = config.get_val("Web","lastchoosedserver")  # ИП:ПОРТ
        nickname = config.get_val("Web","username")  # Никнейм
        args = [str(directory), str(address), "-n "+nickname]
        subprocess.call(args)
        time.sleep(0.05)
    
    def changeUserName(self):
        txt = self.ui.lineEdit.text()
        self.config.set_val("Web","username",str(txt))
        Reestors().changeUserName(str(txt))

class countWindow:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(countWindow, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.count = 0
        
class serverListWidget(QWidget):
    def __init__(self,parent=None):
        super(serverListWidget,self).__init__(parent)
        cfg = Config()
        cfg = cfg.getConfigObj()
        self.count = 0
        servermeta = cfg.get_val("Web",'servers').split(',')
        scroll = QScrollArea()
        scroll2 = QScrollArea()
        listwidget = QWidget()
        widget = QWidget()
        vbox = QVBoxLayout()
        vbox2 =QHBoxLayout()
        hbox = QHBoxLayout()
        self.choose = ChooseServ()

        for i in range(len(servermeta)):
            j = servermeta[i].split(":")
            obj = serversRow(ip=j[0][1:],port=j[1].strip("'"))
            vbox.addWidget(obj)
            vbox2.addLayout(self.choose.add_buttons(id=i+1))
            

        

        listwidget.setLayout(vbox)
        widget.setLayout(vbox2)


        #Scroll Area Properties
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(listwidget)
        scroll.setStyleSheet(u"background:rgba(0,0,0,0)")
        scroll2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll2.setWidgetResizable(True)
        scroll2.setWidget(widget)
        scroll2.setStyleSheet(u"background:rgba(0,0,0,0)")
        scroll2.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.choose.ui.horizontalLayout_2.addWidget(scroll2)
        hbox.addWidget(scroll)
        self.setLayout(hbox)
        self.c = countWindow()
        
    def mousePressEvent(self,event):
        if self.c.count < 1:
            self.choose.show()
            self.c.count += 1




class SettingsUi(QMainWindow):
    def __init__(self,parent=None):
        super(SettingsUi, self).__init__()
        self.config = Config().getConfigObj()
        self.ui = Ui_SetWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.toolButton.clicked.connect(self.changePath)
        self.ui.pushButton.clicked.connect(lambda: self.go_back())
        self.ui.lineEdit.setText(self.config.get_val("Settings","pathclient"))
        self.ui.pushButton_2.clicked.connect(lambda: self.go_back())

    def go_back(self):
        self.close()
        if self.ui.lineEdit.text() != self.config.get_val("Settings","pathclient"):
            self.config.set_val("Settings","pathclient",str(self.ui.lineEdit.text()))

    def changePath(self):
        self.p = findClientDialog().path()
        Reestors().changeClientPath(str(self.p))
        self.ui.lineEdit.setText(str(self.p))

 

class ChooseServ(QDialog):
    def __init__(self,parent=None):
        super(ChooseServ, self).__init__(parent)


        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.WindowStaysOnTopHint)
        self.ui.pushButton_closedialog.clicked.connect(lambda: self.myclose())

    def myclose(self):
        countWindow().count = 0
        self.close

    def add_buttons(self, **args):
        layout = QVBoxLayout()
        line = QFrame()
        btn = QPushButton()
        btn.setObjectName("buttonid" + str(args['id']))

        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        line.setStyleSheet(u"color:white;\n"
        "background:rgba(255,255,255,200); margin-left:25px; margin-right:25px; height:1px")
        font2 = QFont()
        font2.setFamily(u"Montserrat Medium")
        font2.setPointSize(22)
        font2.setBold(False)
        font2.setWeight(50)
        btn.setFont(font2)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        btn.setStyleSheet(u"QPushButton{background: rgba(49,53,47,190); color:white;padding:2px; padding-top:0px; padding-bottom:0px; border-radius:10px} QPushButton:hover{background: rgba(49,53,47,250)}")
        btn.setText(str(args['id']) + "\nCервер "  + "\nВойти")

        layout.addWidget(btn)
        layout.addWidget(line)
        return layout



class serversRow(QWidget):
    def __init__(self, parent=None,**args):
        super(serversRow, self).__init__(parent)
        self.ui = Ui_ServList()
        self.ui.setupUi(self)
        self.setMinimumSize(QtCore.QSize(226, 81))
        self.setMaximumSize(QtCore.QSize(226, 81))

        


        self.server = SAMP(args['ip'],int(args['port']))
        if self.server.get_status() == 'Offline':
            self.ui.indicator.setPixmap(QPixmap(":/ui/red_led.png").scaledToWidth(21))
            self.ui.servername_label.setText('Сервер офлайн')
            self.ui.online_label.setText("Онлайн: 0")
        else:
            self.ui.servername_label.setText(str(self.server.get_serv_hostname()))
            self.ui.online_label.setText(str(self.server.get_serv_players()))
        
       



class setLauncher:
    def __init__(self,launcher,configPath):
        try:
            self.JSONdata = JSONParser("http://127.0.0.1:5000/api")
        except:
            print('Нет интернета мудак')
            sys.exit(app.exec_())

#variable for setup utils

        self.launcher = launcher
        self.reg = Reestors()
        self.config = Config()

#checkupdate
        self.checkUpdate()
#check config return obj if exist
        if self.config.configExist():
            self.config = self.config.getConfigObj()
        else:
            self.config = self.config.generateConfig(
                                    ver=self.launcherver,
                                    lang='ru',
                                    clientPath= str(self.findClient()),
                                    lastServer = self.JSONdata.get_servers_last(),
                                    checksum = self.checkSum(),
                                    UserName = str(self.getUserName()),
                                    clientLink = self.JSONdata.get_download_link_client(),
                                    startup = "False",
                                    servers = str(self.JSONdata.get_servers().strip('[]')))

    def checkUpdate(self):
        launcherVer = self.JSONdata.get_version()
        self.realLauncherVer = self.launcher.ui.label_3.text()
        if launcherVer != re.findall(r'[0-9]+\.[0-9]+\.+[0-9]', self.realLauncherVer)[0]:
            #update Launcher
            pass
        self.launcherver = launcherVer


    def findClient(self):
        if self.reg.clientExist():
            return self.reg.getClientPath()
        else:
            p = self.findClientDialog().path()
            self.config.set_val("Settings","pathclient",str(p))
    def getUserName(self):
        if self.reg.playerNameExist():
            return self.reg.getUserName()
        else:
            return "0"
            
    def checkSum(self):
        return "0"

class findClientDialog(QWidget):
    def __init__(self):
        super(findClientDialog, self).__init__()
        self.p = QFileDialog.getOpenFileName(self," File dialog ",None,"Client (*.exe)")
        self.show()

    def path(self):
        return self.p[0]


class Reestors:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Reestors, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        try:
            self.regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\SAMP',0,winreg.KEY_ALL_ACCESS)
        except:
            print("установи клиент")

    def clientExist(self):
        if self.getClientPath():
            return True
        else:
            return False

    def lastServerExist(self):
        if self.getLastServer():
            return True
        else:
            return False
    def playerNameExist(self):
        if self.getUserName():
            return True
        else:
            return False

    def getLastServer(self):
        try:
            key = winreg.EnumValue(self.regKey,2)[1]
            winreg.CloseKey(self.regKey)
            return key
        except:
            return False


    def getClientPath(self):
        try:
            clientPath = winreg.EnumValue(self.regKey,0)[1]
            winreg.CloseKey(self.regKey)
            return str(clientPath)
        except:
            return False

    def getUserName(self):
        try:
            userName = winreg.EnumValue(self.regKey,1)[1]
            winreg.CloseKey(self.regKey)
            return userName
        except:
            return False

    def changeClientPath(self,new_path):
        try:
            winreg.SetValueEx(self.regKey, 'gta_sa_exe', None, winreg.REG_SZ, str(new_path))
            winreg.CloseKey(self.regKey)
            return new_path
        except:
            return False

    def changeLastServer(self,new_data):
        try:
            winreg.SetValueEx(self.regKey, 'LastServer', None, winreg.REG_SZ, str(new_data))
            winreg.CloseKey(self.regKey)
            return new_data
        except:
            return False
    def changeUserName(self,new_user):
        try:
            winreg.SetValueEx(self.regKey, 'PlayerName', None, winreg.REG_SZ, str(new_user))
            winreg.CloseKey(self.regKey)
            return new_user
        except:
            return False

class Config:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.path = BASE_DIR.joinpath("config.ini")
        self.conf = Configurator()

    def configExist(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

    def generateConfig(self,**args):
        self.conf.create_config(args)
        return self.conf

    def getConfigObj(self):
        return self.conf














if __name__ == "__main__":
    app = QApplication(sys.argv)
    confPath = BASE_DIR.joinpath("config.ini")
    window = Launcher(confPath)


    #setLauncher(window,confPath)



    window.show()

    sys.exit(app.exec_())
