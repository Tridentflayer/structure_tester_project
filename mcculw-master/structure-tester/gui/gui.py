import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

def clicked():
    print('test')


#class QWidgets:

#    def window(self, event, QWidgets):
#        QWidgets.b1(event.rect(), Qt.AlignCenter, self.b1)

#    def paintEvent(self, event):
#        QWidgets.b1

#REEEEEEEEEEEEEEEEEEEEE
def window(self, QWidgets):
    b1 = QtWidgets.QLabel(self)
    b1.setText('CLICK')
    b1.clicked.connect(clicked)

class test(QWidget):



    def __init__(self):
        super().__init__()

        self.initUI()
        self.show()

    def initUI(self):

        self.text = 'test'
        self.label = QtWidgets.QLabel(self)
        self.label.setText('label test')
        self.label.move(50, 50)
        self.setGeometry(200, 200, 400, 600)
        self.setWindowTitle('Test Window')
        self.show()
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('button lol')
        self.b1.clicked.connect(clicked)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp, QApplication, QWidgets)
        qp.end()

    def drawText(self, event, qp, QApplication, QWidgets):
        qp.setPen(QColor(125, 50, 90))
        qp.setFont(QFont('Lobster', 40))
        qp.drawText(event.rect(), Qt.AlignHCenter, self.text)

def main():
    app = QApplication(sys.argv)
    ex = test(),
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()