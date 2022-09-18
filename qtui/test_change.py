# -*- coding: utf-8 -*-
from random import randint
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app_name='小程序'
top=['主菜单1','主菜单2','主菜单3']
tab=['子菜单1', '子菜单2', '子菜单3','子菜单4','子菜单5']

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
        warn_btn = TabButton(warn,top[0])
        self.setItemWidget(warn, warn_btn)
        # 被折叠控件
        warn_item = QListWidgetItem(self)
        # 通过按钮的选中来隐藏下面的item
        warn_btn.toggled.connect(warn_item.setHidden)
        self.warn_widget=LeftWidget(warn_item, tab[:3])
        self.setItemWidget(warn_item,self.warn_widget)
        warn_item.setHidden(True)#默认不展开

        device= QListWidgetItem(self)
        device_btn = TabButton(device, top[1])
        self.setItemWidget(device, device_btn)
        # 被折叠控件
        device_item = QListWidgetItem(self)
        # 通过按钮的选中来隐藏下面的item
        device_btn.toggled.connect(device_item.setHidden)
        self.device_widget=LeftWidget(device_item, [tab[3]])
        self.setItemWidget(device_item, self.device_widget)
        device_item.setHidden(True)  # 默认不展开

        system = QListWidgetItem(self)
        system_btn = TabButton(system, top[2])
        self.setItemWidget(system, system_btn)
        # 被折叠控件
        system_item = QListWidgetItem(self)
        # 通过按钮的选中来隐藏下面的item
        system_btn.toggled.connect(system_item.setHidden)
        self.system_widget=LeftWidget(system_item, [tab[4]])
        self.setItemWidget(system_item,self.system_widget)
        system_item.setHidden(True)  # 默认不展开


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.available_geometry = QDesktopWidget().availableGeometry()
        init_width = self.available_geometry.width() * 0.85
        init_height = self.available_geometry.height() * 0.85
        self.setWindowTitle(app_name)
        self.resize(init_width, init_height)
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
        for i in range(5):
            label = QLabel('这是页面 %d' % i, self)
            label.setAlignment(Qt.AlignCenter)
            # 此处加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
            label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
                randint(0, 255), randint(0, 255), randint(0, 255)))
            self.StackDataDisplay.addWidget(label)
        self.listWidget.warn_widget.update_.connect(self.update_tab)
        self.listWidget.device_widget.update_.connect(self.update_tab)
        self.listWidget.system_widget.update_.connect(self.update_tab)
        ###################
        self.mainLayout.addWidget(self.listWidget)
        self.mainLayout.addWidget(self.StackDataDisplay)

    def update_tab(self,text):
        self.StackDataDisplay.setCurrentIndex(tab.index(text))#根据文本设置不同的页面

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
