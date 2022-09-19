# -*- coding: utf-8 -*-
from random import randint
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


APP_NAME = '千里眼'
TOP = ['千里眼菜单']
MENU = ['首页', '交易记录', '绑定API', '服务与帮助']

NAME_LIST = ["BTC", "ETH", "LINK", "DOT", "EOS", "TRX", "ADA", "LTC", "BCH", "XRP", "BSV", "ETC", "FIL"]



class LeftWidget(QWidget):
    update_ = pyqtSignal(str)
    def __init__(self, item,factor,parent=None):
        super(LeftWidget, self).__init__(parent)
        self.item = item
        layout = QFormLayout(self)
        self.button1 = QPushButton(factor[0])
        layout.addRow(self.button1)
        self.button1.clicked.connect(self.onClick)
        if len(factor) >=3:
            self.button2 = QPushButton(factor[1])
            self.button3 = QPushButton(factor[2])
            layout.addRow(self.button2)
            layout.addRow(self.button3)
            self.button2.clicked.connect(self.onClick)
            self.button3.clicked.connect(self.onClick)
            if len(factor)>=4:
                self.button4 = QPushButton(factor[3])
                layout.addRow(self.button4)
                self.button4.clicked.connect(self.onClick)

    def onClick(self):
        txt = self.sender().text()#获取发送信号的控件文本
        self.update_.emit(txt)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(LeftWidget, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))

class TabButton(QPushButton):
    # 按钮作为开关
    def __init__(self, item,name,parent=None):
        super(TabButton, self).__init__(parent)
        self.item = item
        self.setCheckable(True)  # 设置可选中
        self.setText(name)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(TabButton, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class LeftWindow(QListWidget):
    def __init__(self, *args, **kwargs):
        super(LeftWindow, self).__init__(*args, **kwargs)
        warn = QListWidgetItem(self)
        warn_btn = TabButton(warn, TOP[0])
        self.setItemWidget(warn, warn_btn)
        # 被折叠控件
        warn_item = QListWidgetItem(self)
        # 通过按钮的选中来隐藏下面的item
        # warn_btn.toggled.connect(warn_item.setHidden)
        self.menu_widget=LeftWidget(warn_item, MENU)
        self.setItemWidget(warn_item,self.menu_widget)
        warn_item.setHidden(False)#默认不展开


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.available_geometry = QDesktopWidget().availableGeometry()
        init_width = self.available_geometry.width() * 0.85
        init_height = self.available_geometry.height() * 0.85
        self.setWindowTitle(APP_NAME)
        self.resize(int(init_width), int(init_height))
        # 实例化状态栏，设置状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.mainLayout = QHBoxLayout(self.centralwidget)#全局横向

        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)  # 去除控件间的间隙
        #################
        self.listWidget = LeftWindow()  # 左侧列表
        self.listWidget.setMaximumWidth(150)
        self.listWidget.setMinimumWidth(150)
        # 去掉边框
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.StackDataDisplay = QStackedWidget()  # 右侧层叠窗口
        # 再模拟几个右侧的页面
        # for i in range(5):
        #     label = QLabel('这是页面 %d' % i, self)
        #     label.setAlignment(Qt.AlignCenter)
        #     # 此处加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
        #     label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
        #         randint(0, 255), randint(0, 255), randint(0, 255)))
        #     self.StackDataDisplay.addWidget(label)

        self.StackDataDisplay.addWidget(self.page1())
        self.StackDataDisplay.addWidget(self.page2())
        self.StackDataDisplay.addWidget(self.page3())
        self.StackDataDisplay.addWidget(self.page4())
        self.listWidget.menu_widget.update_.connect(self.update_tab)


        self.mainLayout.addWidget(self.listWidget)
        self.mainLayout.addWidget(self.StackDataDisplay)

    def update_tab(self, text):
        self.StackDataDisplay.setCurrentIndex(MENU.index(text))#根据文本设置不同的页面

    def page1(self):

        # 设置第一个面板
        form1 = QWidget()
        # formLayout1 = QHBoxLayout(form1)

        label = QLabel(form1)
        label.setGeometry(QRect(50, 50, 52, 31))
        # label.setStyleSheet("color:#f4f9ff;\n"
        #                          "font:12pt \'Arial\';\n"
        #                          "border-radius: 10px;\n"
        #                          "background: #171B2B;")
        label.setObjectName("label")
        # _translate = QCoreApplication.translate
        label.setText("  币种")

        self.comboBox_0 = QComboBox(form1)
        self.comboBox_0.setGeometry(QRect(100, 50, 111, 31))
        # self.comboBox_0.setStyleSheet("color:#f4f9ff;\n"
        #                               "font:12pt \'Arial\';\n"
        #                               "border-radius: 10px;\n"
        #                               "background: green;")
        self.comboBox_0.setObjectName("comboBox_0")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")

        i = 0
        for item in NAME_LIST:
            self.comboBox_0.setItemText(i,  item)
            i += 1


        label_1 = QLabel(form1)
        label_1.setGeometry(QRect(270, 50, 71, 31))
        # label_1.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_1.setObjectName("label_1")
        label_1.setText("开单方向")

        comboBox_1 = QComboBox(form1)
        comboBox_1.setGeometry(QRect(360, 50, 111, 31))
        # self.comboBox_1.setStyleSheet("color:#f4f9ff;\n"
        #                               "font:12pt \'Arial\';\n"
        #                               "border-radius: 10px;\n"
        #                               "background: green;")
        comboBox_1.setObjectName("comboBox_1")
        comboBox_1.addItem("")
        comboBox_1.addItem("")
        # self.comboBox_1.addItem("")
        # self.comboBox_1.addItem("")

        comboBox_1.setItemText(0, "开多")
        comboBox_1.setItemText(1,  "开空")
        # self.comboBox_1.setItemText(2, _translate("MainWindow", "_CQ"))


        label_2 = QLabel(form1)
        label_2.setGeometry(QRect(561, 50, 52, 31))
        # label_3.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_2.setObjectName("label_2")
        label_2.setText("K线数据")

        lineEdit_2 = QLineEdit(form1)
        lineEdit_2.setGeometry(QRect(640, 50, 111, 31))
        lineEdit_2.setStyleSheet("font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: white;")
        lineEdit_2.setText("")
        lineEdit_2.setObjectName("lineEdit_2")

        label_4 = QLabel(form1)
        label_4.setGeometry(QRect(30, 120, 52, 31))
        # label_4.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_4.setObjectName("label_4")
        label_4.setText("止盈利差")

        lineEdit_4 = QLineEdit(form1)
        lineEdit_4.setGeometry(QRect(100, 120, 111, 31))
        lineEdit_4.setStyleSheet("font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: white;")
        lineEdit_4.setText("")
        lineEdit_4.setObjectName("lineEdit_4")




        label_5 = QLabel(form1)
        label_5.setGeometry(QRect(270, 120, 71, 31))
        # label_5.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_5.setObjectName("label_5")
        label_5.setText("补仓利差")

        lineEdit_5 = QLineEdit(form1)
        lineEdit_5.setGeometry(QRect(360, 120, 111, 31))
        lineEdit_5.setStyleSheet("font:12pt \'Arial\';\n"
                                       "border-radius: 10px;\n"
                                       "background: white;")
        lineEdit_5.setText("")
        lineEdit_5.setObjectName("lineEdit_5")



        label_6 = QLabel(form1)
        label_6.setGeometry(QRect(561, 120, 61, 31))
        # label_6.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_6.setObjectName("label_6")
        label_6.setText("补仓金额")
        lineEdit_6 = QLineEdit(form1)
        lineEdit_6.setGeometry(QRect(640, 120, 111, 31))
        lineEdit_6.setStyleSheet("font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: white;")
        lineEdit_6.setText("")
        lineEdit_6.setObjectName("lineEdit_6")


        return form1



    def page2(self):
        # 设置第二个面板
        form2 = QWidget()
        formLayout2 = QHBoxLayout(form2)

        label2 = QLabel()
        label2.setText("第二个面板")
        label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(QFont("Roman times", 50, QFont.Bold))
        formLayout2.addWidget(label2)
        return form2

    def page3(self):
        # 设置第三个面板
        form3 = QWidget()
        formLayout3 = QHBoxLayout(form3)
        label3 = QLabel()
        label3.setText("第三个面板")
        label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        label3.setAlignment(Qt.AlignCenter)
        label3.setFont(QFont("Roman times", 50, QFont.Bold))
        formLayout3.addWidget(label3)

        return form3

    def page4(self):

        # 设置第四个面板
        form4 = QWidget()
        formLayout4 = QHBoxLayout(form4)
        label4 = QLabel()
        label4.setText("第四个面板")
        label4.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        label4.setAlignment(Qt.AlignCenter)
        label4.setFont(QFont("Roman times", 50, QFont.Bold))
        formLayout4.addWidget(label4)

        return form4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
