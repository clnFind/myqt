# -*- coding: utf-8 -*-

import sys
import socket
import numpy as np
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton



class SineWaveSender(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sine Wave UDP Sender")
        self.setGeometry(100, 100, 400, 300)

        self.ip_address = ""
        self.port = 9999
        self.frequency = 50  # Hz
        self.amplitude = 1.0  # Volts
        self.channel_count = 1
        self.is_sending = False

        # Create UI elements
        self.init_ui()

        # Create UDP socket
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        # Input fields for IP address, port, frequency, amplitude, and channel count
        self.ip_input = QLineEdit(self)
        self.port_input = QLineEdit(self)
        self.frequency_input = QLineEdit(self)
        self.amplitude_input = QLineEdit(self)
        self.channel_count_input = QLineEdit(self)

        # Set default values
        self.ip_input.setText("127.0.0.1")
        self.port_input.setText(str(self.port))
        self.frequency_input.setText(str(self.frequency))
        self.amplitude_input.setText(str(self.amplitude))
        self.channel_count_input.setText(str(self.channel_count))

        form_layout.addRow("IP Address:", self.ip_input)
        form_layout.addRow("Port:", self.port_input)
        form_layout.addRow("Frequency (Hz):", self.frequency_input)
        form_layout.addRow("Amplitude (V):", self.amplitude_input)
        form_layout.addRow("Channel Count:", self.channel_count_input)

        # Buttons for Start/Stop sending sine wave
        self.start_button = QPushButton("Start Sending", self)
        self.stop_button = QPushButton("Stop Sending", self)

        self.start_button.clicked.connect(self.start_sending)
        self.stop_button.clicked.connect(self.stop_sending)

        self.stop_button.setEnabled(False)  # Stop button initially disabled

        layout.addLayout(form_layout)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def start_sending(self):
        # Read input values
        self.ip_address = self.ip_input.text()
        self.port = int(self.port_input.text())
        self.frequency = float(self.frequency_input.text())
        self.amplitude = float(self.amplitude_input.text())
        self.channel_count = int(self.channel_count_input.text())

        self.is_sending = True
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        # Start a new thread for sending sine wave
        self.sending_thread = threading.Thread(target=self.send_sine_wave)
        self.sending_thread.daemon = True
        self.sending_thread.start()

    def stop_sending(self):
        self.is_sending = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def send_sine_wave(self):
        # Calculate time step
        sample_rate = 1000  # Samples per second
        time_step = 1.0 / sample_rate
        t = 0.0

        while self.is_sending:
            # Generate sine wave data
            for channel in range(self.channel_count):
                sine_value = self.amplitude * np.sin(2 * np.pi * self.frequency * t)
                # message = f"Channel {channel + 1}: {sine_value:.4f}"
                message = f"{sine_value:.4f}"

                # Send message over UDP
                self.udp_socket.sendto(message.encode('utf-8'), (self.ip_address, self.port))

            # Update time and control the frequency
            t += time_step

    def closeEvent(self, event):
        self.is_sending = False
        self.udp_socket.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SineWaveSender()
    window.show()
    sys.exit(app.exec_())