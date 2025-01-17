import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)
win = QMainWindow()
# xy坐标（400，400），长宽（400，300）
win.setGeometry(400, 400, 400, 300)
win.setWindowTitle("Pyqt5 Test")
# Label Text
label = QLabel(win)
label.resize(200, 100)
label.setText("Hey, this is Pyqt5")
label.move(100, 100)
win.show()
sys.exit(app.exec_())

