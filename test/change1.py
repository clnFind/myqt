# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome

APP_NAME = '千里眼'
NAME_LIST = ["BTC", "ETH", "LINK", "DOT", "EOS", "TRX", "ADA", "LTC", "BCH", "XRP", "BSV", "ETC", "FIL"]


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.showselect = 0

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
        self.dataDisplay.addWidget(self.page1())
        # self.init_right()  # 初始化右侧空间

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.dataDisplay, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
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

    def init_left(self):
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
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

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), " 首页")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), " 绑定API")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), " 交易记录")
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

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 8, 0, 1, 3)


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

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def click_mini(self):
        self.showMinimized()  # 最小化

    def click_close(self):
        self.close()

    def click_max(self):
        # print(self.showselect)
        self.showselect = self.showselect + 1
        if self.showselect % 2 != 0:
            self.showMaximized()  # 缩放 最大
        else:
            self.showNormal()


    def page1(self):

        # 设置第一个面板
        form1 = QtWidgets.QWidget()
        form1.setObjectName('right_widget')
        # formLayout1 = QHBoxLayout(form1)

        label = QtWidgets.QLabel(form1)
        label.setGeometry(QtCore.QRect(50, 50, 52, 31))
        # label.setStyleSheet("color:#f4f9ff;\n"
        #                          "font:12pt \'Arial\';\n"
        #                          "border-radius: 10px;\n"
        #                          "background: #171B2B;")
        label.setObjectName("label")
        # _translate = QCoreApplication.translate
        label.setText("  币种")

        self.comboBox_0 = QtWidgets.QComboBox(form1)
        self.comboBox_0.setGeometry(QtCore.QRect(100, 50, 111, 31))
        self.comboBox_0.setStyleSheet("color:#171B2B;\n"
                                      "font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: #E0E0E0;")
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


        label_1 = QtWidgets.QLabel(form1)
        label_1.setGeometry (QtCore.QRect(270, 50, 71, 31))
        # label_1.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_1.setObjectName("label_1")
        label_1.setText("开单方向")

        comboBox_1 = QtWidgets.QComboBox(form1)
        comboBox_1.setGeometry (QtCore.QRect(360, 50, 111, 31))
        comboBox_1.setStyleSheet("color:#171B2B;\n"
                                      "font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: #E0E0E0;")
        comboBox_1.setObjectName("comboBox_1")
        comboBox_1.addItem("")
        comboBox_1.addItem("")
        # self.comboBox_1.addItem("")
        # self.comboBox_1.addItem("")

        comboBox_1.setItemText(0, "开多")
        comboBox_1.setItemText(1,  "开空")
        # self.comboBox_1.setItemText(2, _translate("MainWindow", "_CQ"))


        label_2 = QtWidgets.QLabel(form1)
        label_2.setGeometry (QtCore.QRect(561, 50, 52, 31))
        # label_3.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_2.setObjectName("label_2")
        label_2.setText("K线数据")

        lineEdit_2 = QtWidgets.QLineEdit(form1)
        lineEdit_2.setGeometry (QtCore.QRect(640, 50, 111, 31))
        lineEdit_2.setStyleSheet("font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: white;")
        lineEdit_2.setText("")
        lineEdit_2.setObjectName("lineEdit_2")

        label_4 = QtWidgets.QLabel(form1)
        label_4.setGeometry (QtCore.QRect(30, 120, 52, 31))
        # label_4.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_4.setObjectName("label_4")
        label_4.setText("止盈利差")

        lineEdit_4 = QtWidgets.QLineEdit(form1)
        lineEdit_4.setGeometry (QtCore.QRect(100, 120, 111, 31))
        lineEdit_4.setStyleSheet("font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: white;")
        lineEdit_4.setText("")
        lineEdit_4.setObjectName("lineEdit_4")




        label_5 = QtWidgets.QLabel(form1)
        label_5.setGeometry (QtCore.QRect(270, 120, 71, 31))
        # label_5.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_5.setObjectName("label_5")
        label_5.setText("补仓利差")

        lineEdit_5 = QtWidgets.QLineEdit(form1)
        lineEdit_5.setGeometry (QtCore.QRect(360, 120, 111, 31))
        lineEdit_5.setStyleSheet("font:12pt \'Arial\';\n"
                                       "border-radius: 10px;\n"
                                       "background: white;")
        lineEdit_5.setText("")
        lineEdit_5.setObjectName("lineEdit_5")



        label_6 = QtWidgets.QLabel(form1)
        label_6.setGeometry (QtCore.QRect(561, 120, 61, 31))
        # label_6.setStyleSheet("color:#f4f9ff;\n"
        #                            "font:12pt \'Arial\';\n"
        #                            "border-radius: 10px;\n"
        #                            "background: #171B2B;")
        label_6.setObjectName("label_6")
        label_6.setText("补仓金额")
        lineEdit_6 = QtWidgets.QLineEdit(form1)
        lineEdit_6.setGeometry (QtCore.QRect(640, 120, 111, 31))
        lineEdit_6.setStyleSheet("font:12pt \'Arial\';\n"
                                      "border-radius: 10px;\n"
                                      "background: white;")
        lineEdit_6.setText("")
        lineEdit_6.setObjectName("lineEdit_6")

        form1.setStyleSheet('''
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
                  QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
                    }
                ''')



        return form1


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()