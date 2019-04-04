from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from painter import *
import draw
import Log
import tools
from dxfwrite import DXFEngine as dxf

class SecondWindow(QWidget):

    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(850, 900)
        # window_pale = QtGui.QPalette()
        # window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("C://Users/Yuusha/Desktop/bg.jpg")))
        # self.setPalette(window_pale)
        self.S = 1
        self.x = 1
        self.rate = 1
        self.res = []
        self.painter = PaintBoard(self)
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

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, '保存文件', 'C://Users//Yuusha//Desktop//data2',"dxf文件|*.dxf")
        print(filename[0])
        self.lineEdit4.setText(filename[0])

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
        self.qtable.resize(800, 500)
        self.qtable.setColumnCount(10)
        self.qtable.setRowCount(10)
        self.qtable.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.qtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.qtable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.Vlayout = QVBoxLayout(self)
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout3 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

        self.Hlayout2.addWidget(self.painter)

        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setFixedHeight(32)
        self.lineEdit4.setFixedWidth(300)
        # self.lineEdit4.setFont(lineEditFont)
        self.lineEdit4.setMaxLength(100)

        self.select = QPushButton("保存文件")
        self.select.setFixedWidth(100)
        self.select.setFixedHeight(40)
        # self.select.setFont(labelFont)
        # self.formlayout.addRow(self.lineEdit4, self.signIn)
        self.Hlayout3.addWidget(self.select)
        self.Hlayout3.addWidget(self.lineEdit4)

        self.Hlayout3.setSpacing(10)

        self.ok = QPushButton("确定")
        self.ok.setFixedWidth(100)
        self.ok.setFixedHeight(40)
        # self.ok.setFont(labelFont)
        self.Hlayout1.addWidget(self.ok)

        self.Vlayout.addWidget(self.qtable, Qt.AlignTop)
        self.Vlayout.addLayout(self.Hlayout2)
        self.Vlayout.addLayout(self.Hlayout3)

        self.Vlayout.addLayout(self.Hlayout1,Qt.AlignBottom)
        # self.select.clicked.connect(self.select_path)
        self.select.clicked.connect(self.save_file)
        self.ok.clicked.connect(self.work)

        self.qtable.setHorizontalHeaderLabels([" ","L1/m", "L2/m", "L3/m", "L4/m","L5/m", "朝向","面积/m²","平均能耗"," "])
        # self.qtable.setColumnWidth(9,40)
        # self.qtable.setColumnWidth(0,15)

        self.qtable.cb = []
        for i in range(10):
            self.qtable.cb.append(QCheckBox('', self))

        self.qtable.btns = []
        for i in range(10):
            btn = QPushButton("查看")
            btn.setFixedWidth(100)
            btn.setFixedHeight(40)
            self.qtable.btns.append(btn)

        # for i in range(10):
        #     self.qtable.btns[i].clicked.connect(lambda: self.onbtn(i))
        self.qtable.btns[0].clicked.connect(lambda: self.onbtn(0))
        self.qtable.btns[1].clicked.connect(lambda: self.onbtn(1))
        self.qtable.btns[2].clicked.connect(lambda: self.onbtn(2))
        self.qtable.btns[3].clicked.connect(lambda: self.onbtn(3))
        self.qtable.btns[4].clicked.connect(lambda: self.onbtn(4))
        self.qtable.btns[5].clicked.connect(lambda: self.onbtn(5))
        self.qtable.btns[6].clicked.connect(lambda: self.onbtn(6))
        self.qtable.btns[7].clicked.connect(lambda: self.onbtn(7))
        self.qtable.btns[8].clicked.connect(lambda: self.onbtn(8))
        self.qtable.btns[9].clicked.connect(lambda: self.onbtn(9))
            # self.qtable.setCellWidget(i, 8, self.qtable.cb[i])



        # self.qp = QPainter()
        # self.qp.begin(self)

    def onbtn(self,i):
        self.painter.clear()
        print(i)
        ans = self.res[i]
        # points = draw.cal_points(10,10,ans[0]/10,ans[1]/10,ans[2]/10,ans[3]/10,ans[4]/10,ans[5]/10)
        points = draw.cal_points(60, 60, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5])
        for i in range(len(points)):
            points[i] = QPoint(points[i][0],points[i][1])
        print(points)
        self.painter.setPoints(points)
        # qp = QPainter()
        # qp.begin(self.painter.__board)
        # # 自定义的绘画方法
        # self.painter.drawPoints(QPoint(3,4))
        # qp.end()


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
        # res = [[27.0, 63.0, 9.0, 9.0, 18.0, 1,1215,100]]
        res = tools.selectN(total, energy, 10)

        self.setRes(res)
        print(res)
        for i in range(10):
            for j in range(10):
                try:
                    if j == 5:
                        direction = ""
                        if res[i][5] == 1:
                            direction = "S"
                        elif res[i][5] == 2:
                            direction = "SW40°"
                        elif res[i][5] == 3:
                            direction = "SE40°"
                        self.qtable.setItem(i, j+1, QTableWidgetItem(direction))
                    elif j == 8:
                        self.qtable.setCellWidget(i, 9, self.qtable.btns[i])
                    elif j == 9:
                        self.qtable.setCellWidget(i, 0, self.qtable.cb[i])
                    elif j == 7:
                        self.qtable.setItem(i, j + 1, QTableWidgetItem(str(round(res[i][j],3))))
                    elif j == 6:
                        self.qtable.setItem(i, j + 1, QTableWidgetItem(str(round(res[i][j], 2))))
                    else:
                        item = res[i][j]
                        self.qtable.setItem(i,j+1,QTableWidgetItem(str(item)))
                except:
                    self.qtable.setItem(i, j+1, QTableWidgetItem(""))

    def work(self):
        directory = self.lineEdit4.text()
        res = self.getRes()
        print(res)
        cnt = 0
        x1,y1=0,0
        drawing = dxf.drawing(tools.check_filename(directory))
        for i in range(10):
            # print(self.qtable.cb[i].isChecked())
            if self.qtable.cb[i].isChecked():

                cnt += 1
                gap = max(res[i][0], res[i][1],res[i][2],res[i][3], res[i][4])
                draw.draw_single(drawing, x1, y1, res[i][0], res[i][1],res[i][2],res[i][3], res[i][4],res[i][5])
                x1+=1.5*gap
        drawing.save()

        # reply = QMessageBox.information(self,"消息框标题","这是一条消息。",QMessageBox.yes | QMessageBox.No)
        # self.echo(reply)
        self.slotInfo()