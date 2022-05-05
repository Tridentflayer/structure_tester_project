import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib.figure import Figure
from matplotlib.animation import TimedAnimation
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time
import threading
import matplotlib
import itertools as itrt
matplotlib.use("Qt5Agg")


# Don't touch me here
def setCustomSize(x, width, height):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(x.sizePolicy().hasHeightForWidth())
    x.setSizePolicy(sizePolicy)
    x.setMaximumSize(QtCore.QSize(width, height))

# Don't touch me here either you baka
class CustomMainWindow(QtWidgets.QMainWindow):
    # Runs on initialization
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        # Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("my first window")

        # Create FRAME_A
        self.FRAME_A = QtWidgets.QFrame(self)
        self.FRAME_A.setStyleSheet("QWidget { background-color: %s }" % QtGui.QColor(210, 210, 235, 255).name())
        self.LAYOUT_A = QtWidgets.QGridLayout()
        self.FRAME_A.setLayout(self.LAYOUT_A)
        self.setCentralWidget(self.FRAME_A)

        # Place the matplotlib figure
        self.myFig = CustomFigCanvas()
        self.LAYOUT_A.addWidget(self.myFig, *(0, 1))


        # Start a thread processing dataSendLoop adding in addData_callbackFunc
        # The thread is a daemon which means if you end it early, the thread doesn't finish and also ends
        myDataLoop = threading.Thread(name='myDataLoop', target=dataSendLoop, daemon=True, args=(self.addData_callbackFunc, tloop))
        myDataLoop.start()

        # Show the canvas
        self.show()


        # Still trying to figure out what this does
    def addData_callbackFunc(self, value):
        # print("Add data: " + str(value))
        self.myFig.addData(value)


class CustomFigCanvas(FigureCanvas, TimedAnimation):
    # Runs on initialization
    def __init__(self):
        self.addedData = []
        print('Matplotlib Version:', matplotlib.__version__)
        '''Matplot Graph Code'''

        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax1 = self.fig.add_subplot(111)
        self.xlim = 200

        # What is the purpose of this, what does it do, does this create time?
        self.n = np.linspace(0, self.xlim - 1, self.xlim)
        self.y = (self.n * 0.0) + 0

        # Add lines here
        self.line1 = Line2D([], [])
        self.ax1.add_line(self.line1)


        # settings
        # No touchy!
        self.ax1.set_xlabel('time')
        self.ax1.set_ylabel('raw data')
        self.ax1.set_xlim(0, self.xlim)
        self.ax1.set_ylim(0, 100)
        '''Matplot Graph Code'''
        FigureCanvas.__init__(self, self.fig)
        TimedAnimation.__init__(self, self.fig, interval=1, blit=True)
        # End of init code
    def new_frame_seq(self):
        return iter(range(self.n.size))

    def _init_draw(self):
        lines = [self.line1]
        for l in lines:
            l.set_data([], [])

    # Not sure if can touch or not
    def addData(self, value):
        self.addedData.append(value)

    # I think don't touch me here
    def _step(self, *args):
        # Extends the _step() method for the TimedAnimation class.
        try:
            TimedAnimation._step(self, *args)
        except Exception as e:
            self.abc += 1
            print(str(self.abc))
            TimedAnimation._stop(self)
            pass

    def _draw_frame(self, framedata):
        margin = 2
        while(len(self.addedData) > 0):
            self.y = np.roll(self.y, -1)
            self.y[-1] = self.addedData[0]
            del(self.addedData[0])

        self.line1.set_data(self.n[0:self.n.size - margin], self.y[0:self.n.size - margin])
        self._drawn_artists = [self.line1]


# You need to setup a signal slot mechanism, to
# send data to your GUI in a thread-safe way.
# Believe me, if you don't do this right, things
# go very very wrong..

# I SWEAR TO GOD IF YOU TOUCH THIS, THE EARTH WILL FEEL MY HELLFIRE
class Communicate(QtCore.QObject):
    data_signal = QtCore.pyqtSignal(float)

def timeLoop():
    for cnt in itrt.count():
        t = cnt / 10
        # y value inputs
        ps1y = np.log(np.pi * t)
        ps2y = np.log(5 * np.pi * t)
        ps3y = np.log(3 * np.pi * t)
        ps4y = np.log(2 * np.pi * t)
        ds1y = np.log(1.5 * np.pi * t)

        # yields data to move it to run function
        yield t, ps1y, ps2y, ps3y, ps4y, ds1y

tloop = timeLoop()

def dataSendLoop(addData_callbackFunc, data):
        # Setup the signal-slot mechanism.
        # Please don't touch this
        mySrc = Communicate()
        mySrc.data_signal.connect(addData_callbackFunc)


       # Creates infinite loop to emit signal
        while(True):
            t, yps1, yps2, yps3, yps4, yds1 = next(data)
            print(yps1)
            time.sleep(0.1)
            mySrc.data_signal.emit(yps1)  # <- Here you emit a signal!



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Plastique'))
    myGUI = CustomMainWindow()

    sys.exit(app.exec_())

