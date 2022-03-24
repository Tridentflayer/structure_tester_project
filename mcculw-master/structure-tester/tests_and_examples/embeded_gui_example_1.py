import matplotlib
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
matplotlib.use('tkagg')

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        ps1 = np.linspace(0, 1 * np.pi, 100)
        (ln,) = self.ax.plot(ps1, np.log(ps1), animated=True)
        bg = fig.canvas.copy_from_bbox(fig.bbox)
        fig.canvas.draw()
        self.ax.draw_artist(ln)
        fig.canvas.blit(fig.bbox)

        for j in range(200):
            fig.canvas.restore_region(bg)
            ln.set_ydata(np.sin(ps1 + (j / 250) * np.pi))
            self.ax.draw(ln)
            self.ax.draw_artist(ln)
            fig.canvas.blit(fig.bbox)
            fig.canvas.flush_events()


class AppDemo(QWidget)      :
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)

        chart = Canvas(self)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
