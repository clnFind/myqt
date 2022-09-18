# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
import qtawesome
import sys


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''
        初始化整体布局
        '''
        self.resize(1000, 800)
        self.desktopWidth = QApplication.desktop().width()  # 获取当前桌面的宽
        self.desktopHeight = QApplication.desktop().height()  # 获取当前桌面的高

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')  # 对象命名
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        self.init_left()  # 初始化左侧空间
        self.init_right()  # 初始化右侧空间

        # 将初始化完成的左侧、右侧空间加入整体空间的网格布局
        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_mini = QtWidgets.QPushButton("") # 最小化按钮

    def init_left(self):
        '''
        初始化左侧布局
        '''
        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')  # 左侧部件对象命名
        self.left_layout = QGridLayout()  # 创建网格布局对象
        self.left_widget.setLayout(self.left_layout)  # 将左侧部件设置为网格布局



        self.left_label_1 = QtWidgets.QPushButton("每日推荐")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("我的音乐")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music',color='white'),"华语流行")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy',color='white'),"在线FM")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film',color='white'),"热门MV")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home',color='white'),"本地音乐")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download',color='white'),"下载管理")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart',color='white'),"我的收藏")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
        self.left_layout.addWidget(self.left_close, 0, 2,1,1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
        self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

    def init_right(self):
        '''
        初始化右侧布局
        '''
        self.right_widget1 = QWidget()  # 创建右侧界面1
        self.right_layout1 = QGridLayout()  # 创建网格布局对象1
        self.right_widget1.setLayout(self.right_layout1)  # 设置右侧界面1的布局为网格布局
        self.Button1 = QPushButton() # 加一个用来界面跳转的button1
        self.Button1.setText("进入界面2")
        self.right_layout1.addWidget(self.Button1)

        self.right_widget2 = QWidget()  # 创建右侧界面2
        self.right_layout2 = QGridLayout()  # 创建网格布局对象2
        self.right_widget2.setLayout(self.right_layout2)  # 设置右侧界面2的布局为网格布局
        self.Button2 = QPushButton() # 加一个用来界面跳转的button2
        self.Button2.setText("进入界面1")
        self.right_layout2.addWidget(self.Button2)

        # 把切换界面的button和两个跳转函数绑定
        self.Button1.clicked.connect(self.clicked_1)
        self.Button2.clicked.connect(self.clicked_2)

    def clicked_1(self):
        self.right_widget1.hide() # 隐藏界面1
        self.right_widget2.show() # 显示界面2

    def clicked_2(self):
        self.right_widget2.hide() # 隐藏界面2
        self.right_widget1.show() # 显示界面1





def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    MainUi()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
  main()