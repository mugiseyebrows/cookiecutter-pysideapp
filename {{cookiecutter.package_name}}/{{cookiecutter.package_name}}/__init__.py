import sys
{% if cookiecutter.flavour == "pyside6" %}
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtGui import QIcon
{% elif cookiecutter.flavour == "pyqt5" %}
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
{% endif %}
import os
from .resources import qInitResources
from .MainWindow import MainWindow
import sys

def main():
    {% if cookiecutter.flavour == "pyside6" %}

    {% elif cookiecutter.flavour == "pyqt5" %}
    if sys.platform == 'win32' and os.environ.get('QT_PLUGIN_PATH') is None:
        dir_path = os.path.dirname(sys.executable)
        QT_PLUGIN_PATH = os.path.join(dir_path, "Lib\\site-packages\\PyQt5\\Qt5\\plugins")
        if os.path.isdir(QT_PLUGIN_PATH):
            os.environ['QT_PLUGIN_PATH'] = QT_PLUGIN_PATH
    {% endif %}

    app = QApplication(sys.argv[1:])

    icon = QIcon(":/icons/qt.ico")
    app.setWindowIcon(icon)

    if sys.platform == 'win32':
        try:
            import ctypes
            myappid = "{{cookiecutter.package_name}}"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except ImportError:
            pass

    widget = MainWindow()
    widget.setWindowTitle("{{cookiecutter.package_name}}")
    widget.show()
    sys.exit(app.exec_())

