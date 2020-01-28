from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint
import ui_designer1


class WidgetRules(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('widgetRules.ui', self)
        self.pushButton.clicked.connect(self.ok)

    def ok(self):
        self.next_window = ui_designer1.WidgetNumbSize()
        self.next_window.show()
        self.hide()
