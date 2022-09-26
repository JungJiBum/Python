import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # label
        self.label = QLabel("메시지: ", self)
        self.label.move(10, 10)

        # button
        self.btn = QPushButton("click", self)
        self.btn.move(10, 40)

        # signal-slot
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.label.clear()                  # 지우기
        self.label.setText("버튼 클릭")     # 텍스트 출력


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()