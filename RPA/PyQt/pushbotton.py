from ctypes import windll
from importlib.resources import read_binary
import sys
from urllib.parse import quote_plus
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(300,300,640,480)
        self.setWindowIcon(QIcon("Resources/title-icon.png"))

        self.btn = QPushButton("종료", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.btn_clicked)

        re_btn = QPushButton("사이즈 버튼",self)
        re_btn.move(100,100)
        re_btn.resize(100,100)

        ena_btn = QPushButton("활성화",self)
        ena_btn.move(150,30)
        ena_btn.setEnabled(True)

        Dis_btn = QPushButton("비활성화",self)
        Dis_btn.move(150,60)
        Dis_btn.setDisabled(True)

        tex_btn = QPushButton("텍스트 출력",self)
        tex_btn.move(300,20)
        print(tex_btn.text())

    def btn_clicked(self):
        print("종료합니다.")
        self.close()


print("실행시 등장")
app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
print("종료하면 등장")
