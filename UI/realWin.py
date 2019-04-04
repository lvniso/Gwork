import sys
from PyQt5 import QtGui

from dxfwrite import DXFEngine as dxf
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import hashlib
from PyQt5.QtSql import *

from secondwin import *

class SignInWidget(QWidget):
    is_admin_signal = pyqtSignal()
    is_student_signal = pyqtSignal(str)

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.resize(600, 400)
        # self.setStyleSheet("background: black")
        self.setWindowTitle("demo")
        # window_pale = QtGui.QPalette()
        # window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("C://Users/Yuusha/Desktop/bg.jpg")))
        # self.setPalette(window_pale)
        self.second = SecondWindow()
        self.setUpUI()

    def setUpUI(self):
        self.Vlayout = QVBoxLayout(self)
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        self.formlayout = QFormLayout()
        self.Hlayout3 = QHBoxLayout()
        self.Hlayout4 = QHBoxLayout()

        self.label1 = QLabel("面积(m²): ")
        labelFont = QFont()
        labelFont.setPixelSize(24)
        lineEditFont = QFont()
        lineEditFont.setPixelSize(16)
        self.label1.setFont(labelFont)
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setFixedHeight(32)
        self.lineEdit1.setFixedWidth(100)
        self.lineEdit1.setFont(lineEditFont)
        self.lineEdit1.setMaxLength(10)
        self.label11 = QLabel("m²")
        self.label11.setFont(labelFont)
        self.formlayout.addRow(self.label1, self.lineEdit1)
        self.lineEdit2 = QComboBox()
        self.lineEdit2.addItems(["9.0", "8.7", "8.4", "8.1", "7.8", "7.5", "7.2", "6.9", "6.6", "6.3", "6.0"])  # 添加多个项目
        # self.cb.currentIndexChanged.connect(self.selectionchange)

        self.label2 = QLabel("柱网间距(m): ")
        self.label2.setFont(labelFont)
        # self.lineEdit2 = QLineEdit()
        self.lineEdit2.setFixedHeight(32)
        self.lineEdit2.setFixedWidth(100)
        self.lineEdit2.setFont(lineEditFont)
        # self.lineEdit2.setMaxLength(16)

        self.formlayout.addRow(self.label2, self.lineEdit2)

        self.label3 = QLabel("面积误差(%): ")
        self.label3.setFont(labelFont)
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setFixedHeight(32)
        self.lineEdit3.setFixedWidth(100)
        self.lineEdit3.setFont(lineEditFont)
        self.lineEdit3.setMaxLength(16)

        self.formlayout.addRow(self.label3, self.lineEdit3)

        self.ok = QPushButton("确定")
        self.ok.setFixedWidth(100)
        self.ok.setFixedHeight(30)
        self.ok.setFont(labelFont)
        self.Hlayout4.addWidget(self.ok)

        self.formlayout.setVerticalSpacing(20)
        self.label = QLabel("U型建筑能耗预测")
        fontlabel = QFont()
        fontlabel.setPixelSize(40)
        self.label.setFixedWidth(300)
        # self.label.setFixedHeight(80)
        self.label.setFont(fontlabel)
        self.Hlayout1.addWidget(self.label, Qt.AlignCenter)
        self.widget1 = QWidget()
        self.widget1.setLayout(self.Hlayout1)
        self.widget2 = QWidget()
        self.widget2.setFixedWidth(300)
        self.widget2.setFixedHeight(150)
        self.widget2.setLayout(self.formlayout)
        self.Hlayout2.addWidget(self.widget2, Qt.AlignCenter)
        self.widget = QWidget()
        self.widget.setLayout(self.Hlayout2)
        self.Vlayout.addWidget(self.widget1)
        self.Vlayout.addWidget(self.widget, Qt.AlignTop)
        self.Vlayout.addLayout(self.Hlayout3)
        self.Vlayout.addLayout(self.Hlayout4,Qt.AlignBottom)
        self.ok.clicked.connect(self.work)
        # self.lineEdit2.returnPressed.connect(self.signInCheck)
        # self.lineEdit1.returnPressed.connect(self.signInCheck)




    def slotInfo(self):
        QMessageBox.information(self, "Information",
                                self.tr("字段不能为空!"))
        # self.label.setText("Information MessageBox")

    def work(self):
        S = (self.lineEdit1.text())
        x = (self.lineEdit2.itemText(self.lineEdit2.currentIndex()))
        rate = (self.lineEdit3.text())
        if S == '' or x == '' or rate == '' or S is None or x is None or rate is None:
            self.flag = False
            self.slotInfo()
        else:
            S = int(self.lineEdit1.text())
            x = float(self.lineEdit2.itemText(self.lineEdit2.currentIndex()))
            # x = float(self.lineEdit2.text())
            rate = int(self.lineEdit3.text())
            self.second.setValue(S,x,rate)
            self.second.handle_click()
            # print(self.second.getValue())
            # self.flag = True
            # self.lineEdit1.setText('')
            # self.lineEdit2.setText('')
            # self.lineEdit3.setText('')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    mainMindow = SignInWidget()
    # s = SecondWindow()
    # while mainMindow.flag is False:
    #     mainMindow.work()
    # if mainMindow.flag is True:
    # s.setValue(mainMindow.S, mainMindow.x, mainMindow.rate)


    mainMindow.show()
    sys.exit(app.exec_())