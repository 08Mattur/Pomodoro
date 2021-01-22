# Filename: Main.py
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

def CreateWindow():
    window = QWidget()
    window.setWindowTitle("Pomodoro Tracker")
    window.setGeometry(100,100,300,400)
    window.setStyleSheet('background-color: gray;')
    window.show()
    return window

window = CreateWindow()
sys.exit(app.exec_())
