from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QFontDatabase, QFont
from serial import Serial
import threading
import time

class SerialHandler(QThread):
    """串口读取处理类，使用信号与槽传递数据"""
    data_received = pyqtSignal(dict)  # 定义信号，用于发送数据给主界面

    def __init__(self, port, baud_rate):
        super().__init__()
        self.port = port
        self.baud_rate = baud_rate
        self.running = False
        # self.data_queue = queue.Queue()

    def start(self):
        """启动串口读取线程"""
        self.running = True
        self.thread = threading.Thread(target=self.read_serial_data, daemon=True)
        self.thread.start()

    def stop(self):
        """停止串口读取线程"""
        self.running = False
        if hasattr(self, "thread") and self.thread.is_alive():
            self.thread.join()

    def read_serial_data(self):
        """从串口读取数据并解析"""
        try:
            with Serial(self.port, self.baud_rate, timeout=2) as ser:
                while self.running:
                    raw_data = ser.readline().decode('ascii', errors='ignore').strip()
                    if raw_data:
                        print(f"[蓝牙接收信息]: {raw_data}")
                        parsed_data = self.parse_data(raw_data)
                        # self.data_queue.put(parsed_data)
                        self.data_received.emit(parsed_data)  # 通过信号传递数据
        except Exception as e:
            print(f"串口错误: {e}")

    def parse_data(self, data):
        """解析串口数据"""
        data = data.upper()
        breathing_rate = "0"
        heart_rate = "0"
        fall_status = "无人跌倒"

        # 类型 1 数据解析
        if data.startswith("AA55") and len(data) >= 14:
            try:
                breathing_rate = str(int(data[6:8], 16))  # 呼吸率
                heart_rate = str(int(data[8:10], 16))  # 心率
            except ValueError:
                pass

        # 类型 2 数据解析
        elif data.startswith("AT+NMGS=32"):
            fall_status = "有人跌倒"

        parsed_result = {"呼吸率": breathing_rate, "心率": heart_rate, "跌倒状态": fall_status}
        print(f"解析后的数据: {parsed_result}")
        return parsed_result

    # def get_latest_data(self):
    #     """获取最新数据"""
    #     while not self.data_queue.empty():
    #         latest_data = self.data_queue.get()
    #     return latest_data if "latest_data" in locals() else {"呼吸率": "0", "心率": "0", "跌倒状态": "无人跌倒"}


class DigitalLabel(QLabel):
    """数码管样式的 QLabel"""
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                background-color: black;
                color: red;
                border: 2px solid red;
                padding: 10px;
                border-radius: 5px;
            }
        """)

        # 加载数码字体
        font_path = r"D:\Digital-7 Mono.ttf"  # 替换为你的字体路径
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print(f"无法加载字体: {font_path}")
        else:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            digital_font = QFont(family)
            digital_font.setPointSize(50)  # 设置字体大小
            self.setFont(digital_font)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("监测系统")
        self.setGeometry(100, 100, 800, 600)  # 设置窗口大小
        self.initUI()

        # 串口处理
        self.serial_handler = SerialHandler(port="COM3", baud_rate=115200)

        self.serial_handler.data_received.connect(self.update_ui_with_data)  # 连接信号与槽

        self.serial_handler.start()

        # # 定时器更新数据（2秒间隔）
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_ui_with_data)
        # self.timer.start(2000)  # 每2秒更新一次

        # 定时器处理跌倒状态恢复
        # self.fall_status_reset_timer = QTimer(self)
        # self.fall_status_reset_timer.setSingleShot(True)
        # self.fall_status_reset_timer.timeout.connect(self.reset_fall_status)

        # self.fall_status_override = False  # 用于标记是否处于跌倒状态

    def initUI(self):
        # 主布局
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 添加显示框
        self.respiration_label = self.add_info_row(main_layout, "呼吸率 (bpm)", "0")
        self.heart_rate_label = self.add_info_row(main_layout, "心率 (bpm)", "0")
        self.fall_status_label = self.add_info_row(main_layout, "跌倒状态监测", "无人跌倒")

        # 设置窗口样式
        self.setStyleSheet("background-color: #3e3e3e; color: white;")

    def add_info_row(self, layout, title, value):
        """添加信息行"""
        row_frame = QFrame()
        row_frame.setStyleSheet("border: 2px solid white; margin: 10px;")
        row_layout = QHBoxLayout(row_frame)

        # 标题
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 40, QFont.Bold)
        title_label.setFont(title_font)

        # 数值
        value_label = DigitalLabel(value)
        row_layout.addWidget(title_label, stretch=1)
        row_layout.addWidget(value_label, stretch=1)

        layout.addWidget(row_frame)
        return value_label

    def update_ui_with_data(self, parsed_data):
        """从串口处理器更新数据"""
        # latest_data = self.serial_handler.get_latest_data()
        respiration_rate = parsed_data.get("呼吸率", "0")
        heart_rate = parsed_data.get("心率", "0")
        fall_status = parsed_data.get("跌倒状态", "无人跌倒")

        # 如果是跌倒状态
        # if fall_status == "有人跌倒" and not self.fall_status_override:
        #     self.fall_status_override = True
        #     self.fall_status_label.setText(fall_status)
            # time.sleep(10)
            # self.fall_status_label.setText("无人跌倒")

            # self.fall_status_reset_timer.start(10000)  # 10 秒后恢复
        # 非跌倒状态更新
        # if not self.fall_status_override:

        self.respiration_label.setText(respiration_rate)
        self.heart_rate_label.setText(heart_rate)
        self.fall_status_label.setText(fall_status)

        print(f"界面更新 - 呼吸率: {respiration_rate}, 心率: {heart_rate}, 跌倒状态: {fall_status}")

    # def reset_fall_status(self):
    #     """重置跌倒状态"""
    #     self.fall_status_override = False
    #     self.fall_status_label.setText("无人跌倒")

    def closeEvent(self, event):
        """关闭窗口时释放资源"""
        self.serial_handler.stop()
        super().closeEvent(event)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
