import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtGui import QIcon
import os
from .resources import qInitResources
from .Ui_MainWindow import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self._ui = ui

def main():
    app = QApplication(sys.argv[1:])

    icon = QIcon(":/icons/qt.ico")
    app.setWindowIcon(icon)

    if sys.platform == 'win32':
        import ctypes
        myappid = "{{cookiecutter.package_name}}"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    widget = MainWindow()
    widget.setWindowTitle("{{cookiecutter.package_name}}")
    widget.show()
    sys.exit(app.exec_())

