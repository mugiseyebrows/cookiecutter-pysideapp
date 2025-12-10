from .Ui_MainWindow import Ui_MainWindow

{% if cookiecutter.flavour == "pyside6" %}
from PySide6.QtWidgets import QMainWindow
{% elif cookiecutter.flavour == "pyqt5" %}
from PyQt5.QtWidgets import QMainWindow
{% endif %}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self._ui = ui