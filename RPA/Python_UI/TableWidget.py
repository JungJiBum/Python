import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)

        Header = ["로우1","로우2","로우3"]
        labels = ["컬럼1","컬럼2"]
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.tableWidget.setVerticalHeaderLabels(Header)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))
        
        self.tableWidget.setItem(2, 0, QTableWidgetItem("(2,0)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("(2,1)"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()