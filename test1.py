# coding:utf-8

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# app = QApplication(sys.argv)
# win = QMainWindow()
# # xy坐标（400，400），长宽（400，300）
# win.setGeometry(400, 400, 400, 300)
# win.setWindowTitle("Pyqt5 Test")
# # Label Text
# label = QLabel(win)
# label.resize(200, 100)
# label.setText("Hey, this is Pyqt5")
# label.move(100, 100)
# win.show()
# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化窗口
        self.setGeometry(400, 400, 400, 300)
        self.setWindowTitle("Pyqt5 Test")
        # Button
        self.button = QPushButton(self)
        self.button.resize(200, 100)
        self.button.setText("Hey, Click Me!")
        self.button.move(100, 100)
        # 按钮点击后，执行该按钮上绑定的事件
        self.button.clicked.connect(self.change_text)

    def change_text(self):
        # 修改按钮上的文本
        self.button.setText("Button clicked！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


