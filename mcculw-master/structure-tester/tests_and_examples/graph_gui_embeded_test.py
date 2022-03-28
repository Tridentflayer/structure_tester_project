from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui
import os
import time
import sys
from threading import *
import random
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.PropaanEquivalent = QtGui.QLabel(self.centralwidget)
        self.PropaanEquivalent.setObjectName(_fromUtf8("PropaanEquivalent"))
        self.gridLayout_3.addWidget(self.PropaanEquivalent, 4, 3, 1, 1)
        self.CH4 = QtGui.QLabel(self.centralwidget)
        self.CH4.setObjectName(_fromUtf8("CH4"))
        self.gridLayout_3.addWidget(self.CH4, 2, 3, 1, 1)
        self.CARI = QtGui.QLabel(self.centralwidget)
        self.CARI.setObjectName(_fromUtf8("CARI"))
        self.gridLayout_3.addWidget(self.CARI, 3, 0, 1, 1)
        self.WobbeIndex = QtGui.QLabel(self.centralwidget)
        self.WobbeIndex.setObjectName(_fromUtf8("WobbeIndex"))
        self.gridLayout_3.addWidget(self.WobbeIndex, 2, 0, 1, 1)
        self.WobbeIndexField = QtGui.QLineEdit(self.centralwidget)
        self.WobbeIndexField.setObjectName(_fromUtf8("WobbeIndexField"))
        self.gridLayout_3.addWidget(self.WobbeIndexField, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton.clicked.connect(self.timer)
        self.CARI_Field = QtGui.QLineEdit(self.centralwidget)
        self.CARI_Field.setObjectName(_fromUtf8("CARI_Field"))
        self.gridLayout_3.addWidget(self.CARI_Field, 3, 1, 1, 1)
        self.CH4_field = QtGui.QLineEdit(self.centralwidget)
        self.CH4_field.setObjectName(_fromUtf8("CH4_field"))
        self.gridLayout_3.addWidget(self.CH4_field, 2, 4, 1, 1)
        self.Propaan_field = QtGui.QLineEdit(self.centralwidget)
        self.Propaan_field.setObjectName(_fromUtf8("Propaan_field"))
        self.gridLayout_3.addWidget(self.Propaan_field, 4, 4, 1, 1)
        self.Dichtheid = QtGui.QLabel(self.centralwidget)
        self.Dichtheid.setObjectName(_fromUtf8("Dichtheid"))
        self.gridLayout_3.addWidget(self.Dichtheid, 3, 3, 1, 1)
        self.Verbrandingswaarde = QtGui.QLabel(self.centralwidget)
        self.Verbrandingswaarde.setObjectName(_fromUtf8("Verbrandingswaarde"))
        self.gridLayout_3.addWidget(self.Verbrandingswaarde, 4, 0, 1, 1)
        self.Verbrandingswaarde_field = QtGui.QLineEdit(self.centralwidget)
        self.Verbrandingswaarde_field.setObjectName(_fromUtf8("Verbrandingswaarde_field"))
        self.gridLayout_3.addWidget(self.Verbrandingswaarde_field, 4, 1, 1, 1)
        self.Dichtheid_field = QtGui.QLineEdit(self.centralwidget)
        self.Dichtheid_field.setObjectName(_fromUtf8("Dichtheid_field"))
        self.gridLayout_3.addWidget(self.Dichtheid_field, 3, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 2, 1, 1)
        self.result_field = QtGui.QLineEdit(self.centralwidget)
        self.result_field.setObjectName(_fromUtf8("result_field"))
        self.gridLayout_3.addWidget(self.result_field, 1, 1, 1, 1)
        self.aantalSensoren_label = QtGui.QLabel(self.centralwidget)
        self.aantalSensoren_label.setObjectName(_fromUtf8("aantalSensoren_label"))
        self.gridLayout_3.addWidget(self.aantalSensoren_label, 1, 3, 1, 1)
        self.aantalSensoren_field = QtGui.QLineEdit(self.centralwidget)
        self.aantalSensoren_field.setObjectName(_fromUtf8("aantalSensoren_field"))
        self.gridLayout_3.addWidget(self.aantalSensoren_field, 1, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.dc = MyMplCanvas(MainWindow, width=1, height=2, dpi=100)
        self.gridLayout_3.addWidget(self.dc, 5, 0, 1, 5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.PropaanEquivalent.setText(_translate("MainWindow", "Propaan Equivalent:", None))
        self.CH4.setText(_translate("MainWindow", "CH4:", None))
        self.CARI.setText(_translate("MainWindow", "CARI:", None))
        self.WobbeIndex.setText(_translate("MainWindow", "Wobbe Index:", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.Dichtheid.setText(_translate("MainWindow", "Dichtheid:", None))
        self.Verbrandingswaarde.setText(_translate("MainWindow", "Verbrandingswaarde:", None))
        self.aantalSensoren_label.setText(_translate("MainWindow", "aantal aangesloten sensoren:", None))

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        self.fileQuit()

    def task(self):
        while True:
            ui.dc.update_figure()
            time.sleep(1.0)

    def timer(self):
        t = Timer(1.0, self.task())
        t.start()

def getCO22():
    '''return the CO2 concentration in the atmosphere
    '''
    return 369.56 + random.random()*50


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        # self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyMplCanvas,self).__init__(self.fig)
        self.yAxe = np.array([0])
        self.xAxe = np.array([0])
        self.i = 0

        self.axes = self.fig.add_subplot(111)
        self.axes.autoscale(False)
        #We want the axes cleared every time plot() is called
        self.axes.hold(False)
        self.axes.set_ylim(0, 500)

        self.compute_initial_figure()
        # plt.show(block=False)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def update_figure(self):
        self.yAxe = np.append(self.yAxe, (getCO22()))
        self.xAxe = np.append(self.xAxe, self.i)
        print(self.xAxe, self.yAxe)
        if len(self.yAxe) > 10:
            self.yAxe = np.delete(self.yAxe, 0)

        if len(self.xAxe) > 10:
            self.xAxe = np.delete(self.xAxe, 0)

        self.axes.plot(self.xAxe, self.yAxe)
        self.axes.set_xlim(self.xAxe[0],self.xAxe[len(self.xAxe)-1])
        self.axes.grid(True)

        self.i = self.i + 1

        self.fig.canvas.draw()

# if  __name__ =='__main__':
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())