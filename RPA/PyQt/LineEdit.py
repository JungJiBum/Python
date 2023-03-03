import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(10, 10)
        self.line_edit.textChanged.connect(self.text_changed)

    def text_changed(self):
        text = self.line_edit.text()
        print(text)


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()