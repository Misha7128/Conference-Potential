from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
import ui_designer1


class WidgetWinner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('widgetWinner.ui', self)
        f = open("Tries.txt", "r")
        c = int(f.read()) + 1
        self.label_4.setText('{0} Tries'.format(c))
        self.pushButton.clicked.connect(self.run)
        f.close()

    def run(self):
        self.next_window = ui_designer1.WidgetNumbSize()
        self.next_window.show()
        self.hide()
