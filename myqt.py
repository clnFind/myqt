# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# 绘图设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置字体大小
plt.rcParams.update({'font.size': 10})

APP_NAME = '千里眼'


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.showselect = 0
    # 主窗口初始化
    def init_ui(self):
        # self.setFixedSize(960, 700)
        self.available_geometry = QtWidgets.QDesktopWidget().availableGeometry()
        init_width = self.available_geometry.width() * 0.6
        init_height = self.available_geometry.height() * 0.6
        self.setWindowTitle(APP_NAME)
        self.resize(int(init_width), int(init_height))

        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.init_left()  # 初始化左侧空间

        self.dataDisplay = QtWidgets.QStackedWidget()  # 右侧层叠窗口
        # self.dataDisplay.addWidget(self.page1())
        # self.dataDisplay.addWidget(self.page2())
        self.dataDisplay.addWidget(self.page1())
        self.dataDisplay.addWidget(self.page2())
        # self.init_right()  # 初始化右侧空间

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(self.dataDisplay, 0, 2, 12, 10)  # 右侧部件在第0行第2列，占12行10列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)

        self.main_widget.setStyleSheet('''
                QWidget#left_widget{
                background:#171B2B;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
                }
                ''')
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

    # 左侧窗口初始化
    def init_left(self):
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 全屏按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_mini.clicked.connect(self.click_mini)
        self.left_visit.clicked.connect(self.click_max)
        self.left_close.clicked.connect(self.click_close)

        self.left_label_1 = QtWidgets.QPushButton("千里眼")
        self.left_label_1.setObjectName('left_label')

        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), " 图形生成")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), " 服务与帮助")
        self.left_button_4.setObjectName('left_button')
        # 占位
        self.left_button_5 = QtWidgets.QPushButton()
        self.left_button_5.setObjectName('left_button5')
        self.left_button_6 = QtWidgets.QPushButton()
        self.left_button_6.setObjectName('left_button6')
        self.left_button_7 = QtWidgets.QPushButton()
        self.left_button_7.setObjectName('left_button7')

        # 0, 0, 1, 1 表示第一行第一列，占用1行1列
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 8, 0, 1, 3)

        # self.left_button_1.clicked.connect(self.on_left_button1_clicked)
        # self.left_button_2.clicked.connect(self.on_left_button2_clicked)
        self.left_button_3.clicked.connect(self.on_left_button3_clicked)
        self.left_button_4.clicked.connect(self.on_left_button4_clicked)


        self.left_widget.setStyleSheet('''
          QPushButton{border:none;color:white;}
          QPushButton#left_label{
            border:none;
            border-bottom:1px solid white;
            font-size:18px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
          QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

    # 右侧窗口初始化
    def init_right(self):
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')

    # 菜单图形生成点击跳转
    def on_left_button3_clicked(self):
        # 显示第一个page
        self.dataDisplay.setCurrentIndex(0)

    # 菜单服务与帮助点击跳转
    def on_left_button4_clicked(self):
        # 显示第二个page
        self.dataDisplay.setCurrentIndex(1)

    # 隐藏边框后实现窗口移动
    # 鼠标点击事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    # 鼠标移动事件
    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    # 鼠标释放事件
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    # 窗口最小化
    def click_mini(self):
        self.showMinimized()  # 最小化

    # 窗口关闭
    def click_close(self):
        self.close()

    # 窗口全屏
    def click_max(self):
        # print(self.showselect)
        self.showselect = self.showselect + 1
        if self.showselect % 2 != 0:
            self.showMaximized()  # 缩放 最大
        else:
            self.showNormal()

    # 设置右侧面板
    def page1(self):
        # 设置第1个面板
        form3 = QtWidgets.QWidget()
        form3.setObjectName('right_widget')

        curDateTime = QtCore.QDateTime.currentDateTime()
        label_1 = QtWidgets.QLabel(form3)
        label_1.setGeometry(QtCore.QRect(50, 50, 52, 31))
        label_1.setObjectName("label_1")
        label_1.setText("日期")

        self.start_date = QtWidgets.QLineEdit(form3)
        self.start_date.setGeometry(QtCore.QRect(100, 50, 111, 31))
        self.start_date.setStyleSheet("font:12pt \'Arial\';\n"
                                 "border-radius: 10px;\n"
                                 "background: white;")
        self.start_date.setText(curDateTime.toString("yyyy-MM-dd"))
        self.start_date.setObjectName("lineEdit")

        checkButton = QtWidgets.QPushButton(form3)
        checkButton.setGeometry(QtCore.QRect(700, 50, 60, 31))
        checkButton.setStyleSheet("color:#f4f9ff;\n"
                                 "font:12pt \'Arial\';\n"
                                 "border-radius: 14px;\n"
                                 "background: #171B2B;\n"
                                 "")
        checkButton.setObjectName("pushButton")
        checkButton.setText("生成")

        checkButton.clicked.connect(self.plot_waveform)

        # 清空表格按钮
        clearButton = QtWidgets.QPushButton(form3)
        clearButton.setGeometry(QtCore.QRect(800, 50, 60, 31))
        clearButton.setStyleSheet("color:#f4f9ff; font:12pt 'Arial'; border-radius: 14px; background: #FF5733;")
        clearButton.setObjectName("clearButton")
        clearButton.setText("清空")
        clearButton.clicked.connect(self.clear_table)

        # 创建表格
        self.table = QtWidgets.QTableWidget(1, 1, form3)  # 1 行 1 列
        self.table.setGeometry(QtCore.QRect(60, 120, 800, 400))

        # 填充整个table区域
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(True)

        # 隐藏行列标题
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

        form3.setStyleSheet('''
                                  QWidget#right_widget{
                                    color:#232C51;
                                    background:white;
                                    border-top:1px solid darkGray;
                                    border-bottom:1px solid darkGray;
                                    border-right:1px solid darkGray;
                                    border-top-right-radius:10px;
                                    border-bottom-right-radius:10px;
                                  }
                                  QLineEdit{
                                    border:1px solid gray;
                                    width:300px;
                                    border-radius:10px;
                                    padding:2px 4px;
                                    }
                                ''')
        return form3

    # 绘图
    def plot_waveform(self):  # 设置日期按钮
        # 生成波形数据
        t = np.linspace(0, 1, 500)  # 时间轴
        y = np.sin(2 * np.pi * 5 * t)  # 生成正弦波
        # y = np.sin("yyyyyyyy")

        # 创建图形
        fig, ax = plt.subplots()
        ax.plot(t, y)
        ax.set_title("正弦波")
        ax.set_xlabel("时间 (s)")
        ax.set_ylabel("幅度")
        ax.grid()

        # 嵌入图形到表格中
        canvas = FigureCanvas(fig)
        # 为单元格创建布局
        cell_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(cell_widget)
        layout.addWidget(canvas)

        # 将小部件放入表格单元格
        self.table.setCellWidget(0, 0, cell_widget)
        canvas.draw()  # 绘制图形

    # 表格清空
    def clear_table(self):
        # 清空表格
        self.table.clearContents()
        # self.table.setRowCount(0)  # 也可以选择清空行数

    # 设置右侧面板
    def page2(self):

        # 设置第2个面板
        form4 = QtWidgets.QWidget()
        form4.setObjectName('right_widget')
        formLayout4 = QtWidgets.QHBoxLayout(form4)
        label4 = QtWidgets.QLabel()
        label4.setText("服务与帮助")
        label4.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        label4.setAlignment(QtCore.Qt.AlignCenter)
        label4.setFont(QtGui.QFont("Roman times", 50, QtGui.QFont.Bold))
        formLayout4.addWidget(label4)
        form4.setStyleSheet('''
                                  QWidget#right_widget{
                                    color:#232C51;
                                    background:white;
                                    border-top:1px solid darkGray;
                                    border-bottom:1px solid darkGray;
                                    border-right:1px solid darkGray;
                                    border-top-right-radius:10px;
                                    border-bottom-right-radius:10px;
                                  }

                                ''')
        return form4


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()