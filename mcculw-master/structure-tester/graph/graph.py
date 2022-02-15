import itertools as itrt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# creates figure "ax" with a grid
fig, ax = plt.subplots()
ax.grid()

# creates time
t = []

# sets time as xdata
xdata = t

# ydata inputs
ydataps1 = []
ydataps2 = []
ydataps3 = []
ydataps4 = []
ydatads1 = []

# generates data for the graph
def datagen():
    # creates timer on the x-axis
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

# # creates lines with line-width two, at points t and y[]
lineps1, = ax.plot(t, [], lw=2)
lineps2, = ax.plot(t, [], lw=2)
lineps3, = ax.plot(t, [], lw=2)
lineps4, = ax.plot(t, [], lw=2)
lineds1, = ax.plot(t, [], lw=2)

# init function, clears line data and sets the line data to be t and y[]
def init():
    # clear data
    del xdata[:]
    del ydataps1[:]
    del ydataps2[:]
    del ydataps3[:]
    del ydataps4[:]
    del ydatads1[:]


# set line data to cleared
    lineps1.set_data(xdata, ydataps1)
    lineps2.set_data(xdata, ydataps2)
    lineps3.set_data(xdata, ydataps3)
    lineps4.set_data(xdata, ydataps4)
    lineds1.set_data(xdata, ydatads1)


# return updated values
    return lineps1, lineps2, lineps3, lineps4, lineds1

# updates values for data
def run(data):
    # time (t) and y = data
    t, yps1, yps2, yps3, yps4, yds1 = data
    # update x to be set to time
    xdata.append(t)
    # update ydatas to new y values
    ydataps1.append(yps1)
    ydataps2.append(yps2)
    ydataps3.append(yps3)
    ydataps4.append(yps4)
    ydatads1.append(yds1)


# auto-scaling (kinda)
    xmin, xmax = ax.get_xlim()
    ymin, ymax =ax.get_ylim()

    # compares all y data to ensure the graph scales on the highest value
    ydata_list = [yps1, yps2, yps3, yps4, yds1]
    max_value = max(ydata_list)

    # y scale
    if max_value >= ymax:
        ax.set_ylim(ymin, 2*ymax)
        ax.figure.canvas.draw()

    # Time autoscale
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()

    # updates lines
    lineps1.set_data(xdata, ydataps1)
    lineps2.set_data(xdata, ydataps2)
    lineps3.set_data(xdata, ydataps3)
    lineps4.set_data(xdata, ydataps4)
    lineds1.set_data(xdata, ydatads1)


# returns updated line values
    return lineps1, lineps2, lineps3, lineps4, lineds1

# creates an animation function which runs all the functions in a loop
ani = animation.FuncAnimation(fig, run, datagen, interval=1, init_func=init)

# show graph, absolutely necessary
plt.show()