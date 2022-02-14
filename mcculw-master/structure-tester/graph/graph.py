import itertools as itrt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



# creates figure "ax" with a grid
fig, ax = plt.subplots()
ax.grid()

# creates a line with line-width two, at points x[] and y[]
line, = ax.plot([], [], lw=2)
xdata, ydata = [], []


def data_gen():
    for cnt in itrt.count():
        t = cnt / 10
        yield t, np.log(np.pi*2*t)

    pass

# init function, clears line data and sets the line data to be x[] and y[]
def init():
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

def run(data):
    # time (t) and y = data
    t, y = data
    # update x to be set to time
    xdata.append(t)
    # update y data to new y value
    ydata.append(y)


    # auto-scaling (kinda)
    xmin, xmax = ax.get_xlim()
    ymin, ymax =ax.get_ylim()

    if y >= ymax:
        ax.set_ylim(ymin, 2*ymax)
        ax.figure.canvas.draw()
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, interval=1, init_func=init)

# show graph, absolutely necessary
plt.show()