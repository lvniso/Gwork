from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PaintBoard(QWidget):
    def __init__(self, Parent=None):
        '''
        Constructor
        '''
        super().__init__(Parent)

        self.__InitData()  # 先初始化数据，再初始化界面
        self.__InitView()
        self.points=[]

    def setPoints(self,points):
        self.points = points

    def getPoints(self):
        return self.points

    def __InitData(self):

        self.__size = QSize(200, 200)

        # 新建QPixmap作为画板，尺寸为__size
        self.__board = QPixmap(self.__size)
        self.__board.fill(Qt.white)  # 用白色填充画板

        self.__IsEmpty = True  # 默认为空画板
        self.EraserMode = False  # 默认为禁用橡皮擦模式


        self.__painter = QPainter()  # 新建绘图工具

        self.__thickness = 20  # 默认画笔粗细为10px
        self.__penColor = QColor("black")  # 设置默认画笔颜色为黑色
        # self.__colorList = QColor.colorNames()  # 获取颜色列表

    def __InitView(self):
        # 设置界面的尺寸为__size
        self.setFixedSize(self.__size)

    def clear(self):
        # 清空画板
        self.__board.fill(Qt.white)
        self.update()
        self.__IsEmpty = True

    def ChangePenColor(self, color="black"):
        # 改变画笔颜色
        self.__penColor = QColor(color)

    def ChangePenThickness(self, thickness=10):
        # 改变画笔粗细
        self.__thickness = thickness

    def IsEmpty(self):
        # 返回画板是否为空
        return self.__IsEmpty

    def GetContentAsQImage(self):
        # 获取画板内容（返回QImage）
        image = self.__board.toImage()
        return image


    def paintEvent(self, e):
        self.__painter.begin(self)
        # self.__painter.drawPolyline(QPolygon(self.points))
        self.__painter.drawPixmap(0, 0, self.__board)
        self.__painter.drawPolygon(QPolygon(self.points))
        self.__painter.end()

    # def drawLines(self, qp):
