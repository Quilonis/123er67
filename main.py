from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication, QWidget)


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Testing")
main_win.resize(400, 400)

main_win.show()
app.exec_()
