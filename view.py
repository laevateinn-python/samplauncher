
import sys
from PySide2.QtWidgets import *
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from MainWindow import Ui_MainWindow
from SettingsUi import Ui_SetWindow


class Launcher(QMainWindow):
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)
        self.set_ui = SettingsUi()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_set.clicked.connect(self.set_ui.show)


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






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Launcher()

    window.show()

    sys.exit(app.exec_())
