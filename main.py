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
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap, QFont, QPainter,QPixmap
from MainWindow import Ui_MainWindow
from SettingsUi import Ui_SetWindow
from ServDialog import Ui_Dialog
from ServList import Ui_ServList
import subprocess




BASE_DIR = Path(__file__).resolve().parent

# ==============================UI Classes===============================================


class Launcher(QMainWindow, Ui_MainWindow):
    __instance = None
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.cfg = SetUpLauncher().setUpConfig()
        self.settingspage = Settings.getInstance()

        self.serverlistwidget = serverListWidget.getInstance()
        self.horizontalLayout_3.addWidget(self.serverlistwidget)

        self.label_2.setText(str(countOnline.getInstance().res()))
        self.lineEdit.setText(self.cfg.get_val("Web",'username'))
        self.label_load2.setText("Нечего обновлять")


        # ---------------------------- signals--------------------------------------------
        self.pushButton_set.clicked.connect(lambda: self.settingspage.show())
        self.pushButton_site.clicked.connect(lambda: webbrowser.open(Linker().getWebLink("siteLink")))
        self.pushButton_forum.clicked.connect(lambda: webbrowser.open(Linker().getWebLink("forumLink")))
        self.pushButton_commun.clicked.connect(lambda: webbrowser.open(Linker().getWebLink("communityLink")))
        self.pushButton_shop.clicked.connect(lambda: webbrowser.open(Linker().getWebLink("shopLink")))
        self.pushButton_play.clicked.connect(lambda: Thread(target=self.play(), daemon=True).start())
        self.lineEdit.textEdited.connect(lambda: self.changeUserName())
        # --------------------------------------------------------------------------------
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Launcher()
        return cls.__instance

    def changeUserName(self):
        txt = self.lineEdit.text()
        self.cfg.set_val("Web","username",str(txt))
        Reestors().changePlayerName(str(txt))

    def play(self):

        directory = self.cfg.get_val("Settings","pathclient")
        directory = Path(directory).resolve().parent.joinpath("samp.exe")
        address = self.cfg.get_val("Web","lastchoosedserver").split(":") # ИП:ПОРТ
        nickname = self.cfg.get_val("Web","username")  # Никнейм
        args = [str(directory), "-h=",str(address[0]),"-p=",str(address[1]),"-n=", str(nickname)]
        p = subprocess.Popen(args)

    


class Settings(QMainWindow, Ui_SetWindow):
    __instance = None
    def __init__(self, parent=None):
        
        super(Settings, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.cfg = Config().getConfigObj()

        self.lineEdit.setText(self.cfg.get_val("Settings","pathclient"))
        self.pushButton.clicked.connect(lambda: self.save_exit_page())
        self.toolButton.clicked.connect(lambda: self.changePathClient(findClientWidget().path()))
        self.lineEdit.textEdited.connect(lambda: self.changePathClient(self.lineEdit.text()))

    def save_exit_page(self):
        self.close()
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Settings()
        return cls.__instance

    def changePathClient(self,p):
        p = p
        self.cfg.set_val("Settings","pathclient",p)
        self.lineEdit.setText(p)
        Reestors().changeClientPath(p)


# ========================================================================================

# =============================UI Dialog + UI Widgets=====================================


class chooseServDialog(QDialog,Ui_Dialog):
    __instance = None
    def __init__(self,parent=None):
        super(chooseServDialog, self).__init__(parent)
        
        self.setupUi(self)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.WindowStaysOnTopHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_closedialog.clicked.connect(lambda: self.myclose())

    def myclose(self):
        countWindow().count = 0
        self.close

    def add_buttons(self, **args):
        layout = QVBoxLayout()
        line = QFrame()
        btn = QPushButton()
        btn.setObjectName("buttonid" + str(args['id']))
        self.cfg = Config().getConfigObj()

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
        btn.clicked.connect(lambda: self.func(args['id']))
        layout.addWidget(btn)
        layout.addWidget(line)
        return layout
    def func(self,iter):
        servers = self.cfg.get_val("Web","Servers").split(",")
        servers = servers[iter-1]
        self.cfg.set_val("Web","lastchoosedserver",str(servers))
        Reestors().changeLastServer(str(servers))
        countWindow().count = 0
        self.close()
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = chooseServDialog()
        return cls.__instance
    
        


        

class findClientWidget(QWidget):
    def __init__(self):
        super(findClientWidget, self).__init__()
        self.p = QFileDialog.getOpenFileName(self," File dialog ",None,"Client (gta_sa.exe)")
        self.show()

    def path(self):
        return self.p[0]

class serverListWidget(QWidget):
    __instance = None
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
        self.choose = chooseServDialog()
        self.countOnline = countOnline()
        for i in range(len(servermeta)):
            j = servermeta[i].split(":")
            obj = serversRow(ip=j[0],port=j[1])
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
        self.choose.horizontalLayout_2.addWidget(scroll2)
        hbox.addWidget(scroll)
        self.setLayout(hbox)
        self.c = countWindow()
        
    def mousePressEvent(self,event):
        if self.c.count < 1:
            self.choose.show()
            self.c.count += 1
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = serverListWidget()
        return cls.__instance

class serversRow(QWidget,Ui_ServList):
    __instance = None
    def __init__(self,parent=None,**args):
        super(serversRow, self).__init__(parent)
        
        self.setupUi(self)
        self.setMinimumSize(QtCore.QSize(226, 81))
        self.setMaximumSize(QtCore.QSize(226, 81))
        self.count = countOnline.getInstance()
        

        


        self.server = SAMP(args['ip'],int(args['port']))
        if self.server.get_status() == 'Offline':
            self.indicator.setPixmap(QPixmap(":/ui/red_led.png").scaledToWidth(21))
            self.servername_label.setText('Сервер офлайн')
            self.online_label.setText("Онлайн: 0")
            self.count.add(0)
        else:
            self.servername_label.setText(str(self.server.get_serv_hostname()))
            self.online_label.setText(str(self.server.get_serv_players()))
            self.count.add(int(self.server.get_info().players))
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = serversRow()
        return cls.__instance

        
# ========================================================================================

# ===================================Adapter class========================================
class countOnline:
    __instance = None
    def __init__(self):
        self.count = []

    def add(self,count):
        self.count.append(int(count))

    def res(self):
        return "Общий онлайн: " + str(sum(self.count))
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = countOnline()
        return cls.__instance
        
class countWindow:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(countWindow, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.count = 0

#=========================================================================================

# ===================================SetUp classes========================================

class SetUpLauncher:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SetUpLauncher, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.links = Linker()
        self.reestor = Reestors()
        self.checkUpdateLauncher()
        self.checkUpdateClient()
    
    def setUpConfig(self):
        cfg = Config()
        if cfg.configExist():
            return cfg.getConfigObj()
        else:
            cfg = cfg.generateConfig(ver=self.realLauncherVer,
                                    lang='ru',
                                    clientPath= str(self.getClient()),
                                    lastServer = "",
                                    checksum = self.checkSum(),
                                    UserName = str(self.reestor.getPlayerName()),
                                    clientLink = self.links.getJson().get_download_link_client(),
                                    startup = "False",
                                    servers = str(self.links.getJson().get_servers()))
            return cfg
    def checkSum(self):
        return "0"

    def getClient(self):
        if self.reestor.clientExist():
            return self.reestor.getClientPath()
        else:
            return findClientWidget().path()

    def checkUpdateLauncher(self):
        launcherVer = self.links.getJson().get_version()
        realLauncherVer = Settings.getInstance().label_3.text()
        self.realLauncherVer = re.findall(r'[0-9]+\.[0-9]+\.+[0-9]', realLauncherVer)[0]
        if launcherVer != self.realLauncherVer:
            p = BASE_DIR.joinpath("Launcher.exe")
            args=["updater.exe",p,'-i', 'Launcher']
            subprocess.call(args)
    def checkUpdateClient(self):
        try:
           stat = self.reestor.exception
           l = Launcher.getInstance()
           l.pushButton_play.setStyleSheet(u"QPushButton{\n""background-image: url(:/ui/download.png)}")
           l.pushButton_play.clicked.connect(lambda: subprocess.call(["updater.exe",BASE_DIR.joinpath("Sunrise Games"),'-i',"Client"]))
        except:
            pass
    
    
        




# ===================================Error UI ============================================
class Error(QDialog):
    def __init__(self,text,parent=None):
        super(Error, self).__init__(parent)

        self.setWindowTitle("Error")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        font = QFont()
        font.setFamily(u"Montserrat Medium")
        font.setPointSize(20)

        self.resize(498, 150)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel()
        self.label.setFont(font)
        self.label.setText(text)
        self.pushButton = QPushButton()
        self.pushButton.setText("OK")
        self.pushButton.setFont(font)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.close())
        self.show()
    
# ========================================================================================

# ===================================System clases========================================
class Config:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.path = BASE_DIR.joinpath("config.ini")
        self.cfg = Configurator()

    def configExist(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

    def generateConfig(self,**args):
        self.cfg.create_config(args)
        return self.cfg

    def getConfigObj(self):
        return self.cfg

class Linker:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Linker, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        try:
            self.JSONquery = JSONParser("http://127.0.0.1:5000/api",1)
        except:
            with open(BASE_DIR.joinpath("stockjson.json"),'r') as jsonrec:
                self.JSONquery = JSONParser(json.load(jsonrec),0)
                #Error("Сервер не отвечает на")
    def getWebLink(self,name):
        return str(self.JSONquery.get_web_links()[str(name)])
    
    def getJson(self):
        return self.JSONquery

class Reestors:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Reestors, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        try:
            self.regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\SAMP',0,winreg.KEY_ALL_ACCESS)
        except:
            self.exception = self.returnsmth()
            
    def returnsmth(self):
        return "needupdate" 
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
        if self.getPlayerName():
            return True
        else:
            return False

    def getLastServer(self):
        try:
            key = winreg.EnumValue(self.regKey,2)[1]
            return key
        except:
            return False


    def getClientPath(self):
        try:
            clientPath = winreg.EnumValue(self.regKey,1)[1]
            return str(clientPath)
        except:
            return False

    def getPlayerName(self):
        try:
            userName = winreg.EnumValue(self.regKey,0)[1]
            return userName
        except:
            return False

    def changeClientPath(self,new_path):
        try:
            winreg.SetValueEx(self.regKey, 'gta_sa_exe', None, winreg.REG_SZ, str(new_path))
            return new_path
        except:
            return False

    def changeLastServer(self,new_data):
        try:
            winreg.SetValueEx(self.regKey, 'LastServer', None, winreg.REG_SZ, str(new_data))
            return new_data
        except:
            return False
    def changePlayerName(self,new_user):
        try:
            winreg.SetValueEx(self.regKey, 'PlayerName', None, winreg.REG_SZ, str(new_user))
            return new_user
        except:
            return False
# ===================================MAIN=================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Launcher.getInstance()
    window.show()
    print(BASE_DIR)

    

    sys.exit(app.exec_())
# ========================================================================================
