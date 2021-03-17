
import sys
import os
import webbrowser
import json

from SAMP_model import *
import re
from pathlib import Path
import winreg

from PySide2.QtWidgets import *
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from MainWindow import Ui_MainWindow
from SettingsUi import Ui_SetWindow
from ServDialog import Ui_Dialog


BASE_DIR = Path(__file__).resolve().parent.parent

class Launcher(QMainWindow):
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)
        self.set_ui = SettingsUi()
        self.chooseserv_ui = ChooseServ()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

#signals

        self.ui.pushButton_set.clicked.connect(self.set_ui.show)
        self.ui.pushButton_site.clicked.connect(lambda: webbrowser.open("http://suvorovka-rp.ru"))
        self.ui.pushButton_forum.clicked.connect(lambda: webbrowser.open("http://forum.suvorovka-rp.ru"))
        self.ui.pushButton_commun.clicked.connect(lambda: webbrowser.open("https://vk.com/suvorovka.crmp"))
        self.ui.pushButton_shop.clicked.connect(lambda: webbrowser.open("http://shop.suvorovka-rp.ru"))





class SettingsUi(QMainWindow):
    def __init__(self, parent=None):
        super(SettingsUi, self).__init__(parent)

        self.ui = Ui_SetWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.close()


class ChooseServ(QDialog):
    def __init__(self, parent=None):
        super(ChooseServ, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

class setLauncher:
    def __init__(self,launcher,configPath):
        self.JSONdata = JSONParser("http://127.0.0.1:5000/api")


        self.regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\SAMP')

        self.launcher = launcher

        self.checkUpdate()
        self.config = self.checkConfig(configPath,
                                ver=self.realLauncherVer,
                                lang='ru',
                                clientPath=self.findClient(),
                                checksum = self.checkSum(),
                                UserName = self.getUserName(),
                                clientLink = self.JSONdata.get_download_link_client(),
                                lastServer = self.lastPlayedServer(),
                                startup = "False",
                                servers = "[('localhost',7777)]")

    def checkUpdate(self):
        launcherVer = self.JSONdata.get_version()
        self.realLauncherVer = self.launcher.set_ui.ui.label_3.text()
        if launcherVer != re.findall(r'[0-9]+\.[0-9]+\.+[0-9]', self.realLauncherVer):
            #update Launcher
            pass

    def checkConfig(self,path,**args):
        if os.path.exists(path):
            conf = Configurator(path)
            return conf
        else:
            conf = Configurator(path)
            conf.create_config(args)
            return conf

    def findClient(self):
        clientPath = winreg.EnumValue(self.regKey,0)[1]
        if clientPath:
            winreg.CloseKey(self.regKey)
            return str(clientPath)

        else:
            return self.findClientDialog()


    def checkSum(self):
        return "0"
    def lastPlayedServer(self):
        return "0"
    def getUserName(self):
        return "0"


class findClientDialog(QWidget):
    def __init__(self):
        super(Dialog, self).__init__()
        self.p = QFileDialog.getOpenFileName(self," File dialog ",None,"Client (*.exe)")
        self.show()

    def path(self):
        return self.p[0]







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Launcher()
    setLauncher(window,BASE_DIR.joinpath("config.ini"))


    window.show()

    sys.exit(app.exec_())
