import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class test(QWidget):
    def __init__(self):

            super().__init__()
            self.initUI()
            self.show()



    def initUI(self):

        #graph code

        ps1 = np.linspace(0, 1 * np.pi, 100)
        fig, ax = plt.subplots()
        (ln,) = ax.plot(ps1, np.log(ps1), animated=True)

        plt.show(block=False)
        plt.pause(0.1)
        bg = fig.canvas.copy_from_bbox(fig.bbox)
        ax.draw_artist(ln)
        fig.canvas.blit(fig.bbox)

        for j in range(200):
            fig.canvas.restore_region(bg)
            ln.set_ydata(np.sin(ps1 + (j / 250) * np.pi))
            ax.draw_artist(ln)
            fig.canvas.blit(fig.bbox)
            fig.canvas.flush_events()

        #end of graph code

        #align everything better
        self.grid = QGridLayout()
        #self.grid.addWidget(self.)
        self.setLayout(self.grid)

        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 200)

        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Test Window')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = test()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()