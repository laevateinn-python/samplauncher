
import sys
from PySide2.QtWidgets import *
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from MainWindow import Ui_MainWindow


class Launcher(QMainWindow):
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Launcher()

    window.show()

    sys.exit(app.exec_())
