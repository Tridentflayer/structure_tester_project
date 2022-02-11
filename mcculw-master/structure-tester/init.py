# Example code to pull functions out of a file to be used here
# All code will be run from this file
import sys

from gui.gui import say_hello
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class test(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.text = 'pog'

        self.setGeometry(200, 200, 400, 600)
        self.setWindowTitle('Test Window')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)
        #qp.set

def main():
    app = QApplication(sys.argv)
    ex = test()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()