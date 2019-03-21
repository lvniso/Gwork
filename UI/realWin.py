import sys
from PyQt5 import QtGui

from dxfwrite import DXFEngine as dxf
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import hashlib
from PyQt5.QtSql import *
import draw
import Log

class SignInWidget(QWidget):
    is_admin_signal = pyqtSignal()
    is_student_signal = pyqtSignal(str)

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.resize(600, 400)
        # self.setStyleSheet("background: black")
        self.setWindowTitle("demo")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("C://Users/Yuusha/Desktop/bg.jpg")))
        self.setPalette(window_pale)
        self.second = SecondWindow()
        # self.flag = True
        # self.S = 1
        # self.x = 1
        # self.rate = 1
        self.setUpUI()

    def setUpUI(self):
        self.Vlayout = QVBoxLayout(self)
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        self.formlayout = QFormLayout()
        self.Hlayout3 = QHBoxLayout()
        self.Hlayout4 = QHBoxLayout()

        self.label1 = QLabel("面积: ")
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

        self.formlayout.addRow(self.label1, self.lineEdit1)

        self.lineEdit2 = QComboBox()
        self.lineEdit2.addItems(["9.0", "8.7", "8.4", "8.1", "7.8", "7.5", "7.2", "6.9", "6.6", "6.3", "6.0"])  # 添加多个项目
        # self.cb.currentIndexChanged.connect(self.selectionchange)

        self.label2 = QLabel("柱网间距: ")
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

    # def selectionchange(self, i):
    #     for count in range(self.cb.count()):
    #         self.cb.itemText(count)


    def slotInfo(self):
        QMessageBox.information(self, "Information",
                                self.tr("字段不能为空!"))
        # self.label.setText("Information MessageBox")

    def work(self):
        S = (self.lineEdit1.text())
        x = (self.lineEdit2.text())
        rate = (self.lineEdit3.text())
        if S == '' or x == '' or rate == '' or S is None or x is None or rate is None:
            self.flag = False
            self.slotInfo()
        else:
            S = int(self.lineEdit1.text())
            x = float(self.lineEdit2.text())
            rate = int(self.lineEdit3.text())
            self.second.setValue(S,x,rate)
            self.second.handle_click()
            # print(self.second.getValue())
            self.flag = True
            self.lineEdit1.setText('')
            self.lineEdit2.setText('')
            self.lineEdit3.setText('')


class SecondWindow(QWidget):

    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(1250, 750)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("C://Users/Yuusha/Desktop/bg.jpg")))
        self.setPalette(window_pale)
        self.S = 1
        self.x = 1
        self.rate = 1
        self.res = []

        self.table()


    def handle_click(self):
        if not self.isVisible():
            self.show_data()
            self.show()

    def setRes(self,res):
        self.res = res

    def getRes(self):
        return self.res

    def handle_close(self):
        self.close()

    def select_path(self):
        directory = QFileDialog.getExistingDirectory(self, "选择文件夹", "C://Users//Yuusha//Desktop//data2")
        print(directory)
        self.lineEdit4.setText(directory)

    def setValue(self,S,x,rate):
        self.S = S
        self.x = x
        self.rate = rate
        return S,x,rate

    def getValue(self):
        return self.S,self.x,self.rate

    def table(self):
        self.qtable = QTableWidget(self)
        self.setWindowTitle("表格")
        self.qtable.resize(1200, 700)
        self.qtable.setColumnCount(8)
        self.qtable.setRowCount(10)
        self.Vlayout = QVBoxLayout(self)
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout3 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setFixedHeight(32)
        self.lineEdit4.setFixedWidth(300)
        # self.lineEdit4.setFont(lineEditFont)
        self.lineEdit4.setMaxLength(100)

        self.select = QPushButton("选择目录")
        self.select.setFixedWidth(100)
        self.select.setFixedHeight(30)
        # self.select.setFont(labelFont)
        # self.formlayout.addRow(self.lineEdit4, self.signIn)
        self.Hlayout3.addWidget(self.lineEdit4)
        self.Hlayout3.addWidget(self.select)

        self.ok = QPushButton("确定")
        self.ok.setFixedWidth(100)
        self.ok.setFixedHeight(30)
        # self.ok.setFont(labelFont)
        self.Hlayout1.addWidget(self.ok)

        self.Vlayout.addWidget(self.qtable, Qt.AlignTop)
        self.Vlayout.addLayout(self.Hlayout3)
        self.Vlayout.addLayout(self.Hlayout1,Qt.AlignBottom)
        self.select.clicked.connect(self.select_path)
        self.ok.clicked.connect(self.work)

        self.qtable.setHorizontalHeaderLabels(["L1/m", "L2/m", "L3/m", "L4/m", "朝向","面积/m2","平均能耗",""])
        self.qtable.setColumnWidth(7,15)

        self.qtable.cb = []
        for i in range(10):
            self.qtable.cb.append(QCheckBox('', self))
        for i in range(10):
            self.qtable.setCellWidget(i, 7, self.qtable.cb[i])

        self.qp = QPainter()
        self.qp.begin(self)


    def selectN(self,total, energy, n):
        res = []
        for i in range(len(energy)):
            area = total[i][0] * total[i][1] - total[i][2] * total[i][3]
            ans = energy[i] / area *100
            res.append([total[i][0], total[i][1],total[i][2],total[i][3], total[i][4],area,ans])
        res.sort(key=lambda x: x[6])
        # print(res[:n])
        return res[:n]

    def slotInfo(self):
        QMessageBox.information(self, "Information",
                                self.tr("生成文件成功!"))
        # self.label.setText("Information MessageBox")

    def show_data(self):
        S,x,rate = self.getValue()
        total = draw.cal(S, x, rate * 0.01)
        print(total)
        # print(self.S)
        # total = draw.cal(self.S, self.x, self.rate * 0.01)
        energy = Log.estimation(total)
        # print(energy)
        res = self.selectN(total, energy, 10)
        self.setRes(res)
        for i in range(10):
            for j in range(7):
                if j == 4:
                    direction = "S"
                    if res[i][4] == 2:
                        direction = "SW40°"
                    elif res[i][4] == 3:
                        direction = "SE40°"
                    self.qtable.setItem(i, j, QTableWidgetItem(direction))
                else:
                    self.qtable.setItem(i,j,QTableWidgetItem(str(res[i][j])))

    def work(self):
        directory = self.lineEdit4.text()
        res = self.getRes()
        print(res)
        cnt = 0
        for i in range(10):
            # print(self.qtable.cb[i].isChecked())
            if self.qtable.cb[i].isChecked():
                drawing = dxf.drawing(directory + '/pic' + str(cnt) + '.dxf')
                cnt += 1
                draw.draw_single(drawing, 0, 0, res[i][0], res[i][1],res[i][2],res[i][3], res[i][4])
                drawing.save()

        # reply = QMessageBox.information(self,"消息框标题","这是一条消息。",QMessageBox.yes | QMessageBox.No)
        # self.echo(reply)
        self.slotInfo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    mainMindow = SignInWidget()
    s = SecondWindow()
    # while mainMindow.flag is False:
    #     mainMindow.work()
    # if mainMindow.flag is True:
    # s.setValue(mainMindow.S, mainMindow.x, mainMindow.rate)


    mainMindow.show()
    sys.exit(app.exec_())