from ctypes import windll
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

        #StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("statusBar Test")

        self.spinbox = QSpinBox(self)
        self.spinbox.move(10,10)
        self.spinbox.valueChanged.connect(self.spinbox_value_changed)

    def spinbox_value_changed(self):
        value = self.spinbox.value()
        print(value)


    #     #CheckBox
    #     self.cbox = QCheckBox("미수", self)
    #     self.cbox.move(10,10)
    #     self.cbox.stateChanged.connect(self.slot)

    # def slot(self, state):
    #     if state == Qt.Checked:
    #         print("미수")
    #     else:
    #         print("보통")



    #     #Text Field
    #     self.line_edit = QLineEdit(" ", self)
    #     self.line_edit.move(10,10)
    #     self.line_edit.textChanged.connect(self.text_changed)
        
    # def text_changed(self):
    #     text = self.line_edit.text()    #QLineEdit 위젯에 입력된 텍스트 가져오기
    #     print(text)



        # #label
        # self.label = QLabel("Message : ", self)
        # self.label.move(10,10)

        # #Button
        # self.btn = QPushButton("CLick",self)
        # self.btn.move(10,40)

        # #signal-slot
        # self.btn.clicked.connect(self.btn_clicked)

        # #Image
        # img = QLabel()
        # img.setPixmap(QPixmap("python_logo.png"))
        # self.setCentralWidget(img)
        


    def btn_clicked(self):
        self.label.clear()                  #Clear
        self.label.setText("Button Click")  # Text print
        
        

# print(sys.argv) ['c:\\Users\\tec\\vscode\\python\\Python_UI\\UI.py']
# app = QApplication(sys.argv)
print("실행시 등장")
app = QApplication(["UI.py"])

window = MyWindow()
window.show()

app.exec_()
print("종료하면 등장")
