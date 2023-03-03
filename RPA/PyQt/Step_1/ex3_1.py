import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()  # -> super() 알아보기
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("My First Application")
        self.move(800,400) # move(좌우, 상하) 스크린의 픽셀 위치로조정
        self.resize(800,500) # 위젯의 크기를 너비 400 , 높이 200 으로 조절
        self.show() # 위젯을 스크린에 나타냄


if __name__ == '__main__':  # __name__ -> 현재 모듈의 이름이 저장되는 내장 변수
    app = QApplication(sys.argv)  
    ex = MyApp()
    sys.exit(app.exec_())