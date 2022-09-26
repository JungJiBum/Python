from ctypes import windll
import sys
from urllib.parse import quote_plus
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,400,300)

        btn1 = QPushButton("Button1")
        btn1.clicked.connect(self.text_changed)
        
        btn2 = QPushButton("Button2")
        btn2.clicked.connect(self.text_changed)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

    def text_changed(self):
        print(self.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()        