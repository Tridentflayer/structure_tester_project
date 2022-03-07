import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from graph import graphtest


class test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    def initUI(self):

        self.im = QPixmap(graphtest())
        self.label = QLabel()
        self.label.setPixmap(self.im)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)

        button = QPushButton('graph', self)
        button.setToolTip('shows the graph')
        button.move(100, 70)
        button.clicked.connect(self.on_click2)

        button2 = QPushButton('graph', self)
        button2.setToolTip('definitely shows the graph')
        button2.move(100, 0)
        button2.clicked.connect(self.on_click)

        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 200)

        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Test Window')
        self.show()

    @pyqtSlot()
    def on_click(self):

        print(amogis)

    @pyqtSlot()
    def on_click2(self):

        graphtest()

    def drawText(self, event, qp):
        qp.setPen(QColor(125, 50, 90))
        qp.setFont(QFont('Lobster', 40))
        qp.drawText(event.rect(), Qt.AlignHCenter, self.text, event, qp)

    class Canvas(FigureCanvas):
        def __init__(self, parent):
            fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 200)
            super().__init(fig)
            self.setParent(parent)

def main():
    app = QApplication(sys.argv)
    ex = test(),
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()