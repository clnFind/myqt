import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem

class WaveformTable(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # 创建按钮
        self.plot_button = QPushButton("生成波形图", self)
        self.plot_button.clicked.connect(self.plot_waveform)

        # 创建表格
        self.table_widget = QTableWidget(1, 1, self)  # 1 行 1 列
        self.table_widget.setCellWidget(0, 0, QWidget())  # 在表格中放置一个 QWidget

        # 添加组件到布局
        self.layout.addWidget(self.plot_button)
        self.layout.addWidget(self.table_widget)

    def plot_waveform(self):
        # 生成波形数据
        t = np.linspace(0, 1, 500)  # 时间轴
        y = np.sin(2 * np.pi * 5 * t)  # 生成正弦波

        # 创建图形
        fig, ax = plt.subplots()
        ax.plot(t, y)
        ax.set_title("正弦波")
        ax.set_xlabel("时间 (s)")
        ax.set_ylabel("幅度")
        ax.grid()

        # 嵌入图形到表格中
        canvas = FigureCanvas(fig)
        self.table_widget.cellWidget(0, 0).layout = QVBoxLayout()
        self.table_widget.cellWidget(0, 0).layout.addWidget(canvas)
        canvas.draw()  # 绘制图形

class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("波形图生成器")
        self.setGeometry(100, 100, 400, 300)

        # 初始化波形表
        self.waveform_table = WaveformTable()
        self.setCentralWidget(self.waveform_table)

def main():
    app = QApplication(sys.argv)
    main_window = MainUi()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()