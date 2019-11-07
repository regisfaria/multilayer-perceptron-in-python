import matplotlib.pyplot as plt
import numpy as np
import random as rd
from time import sleep

x = 0
y = 1

plt.ion()

figure = plt.figure()
#subplot(nrows, ncols, index, **kwargs)
ax = figure.add_subplot(111)


line1, = ax.plot(x, y) 
error_list, eras = [], []

for phase in np.linspace(0, 10*np.pi, 500):
    #calc. erro
    for t in range(x, y):
        value = rd.uniform(-1, 1)
        error_list.append(value)
    #era
    for era in range(x, y):
        eras.append(era)
    
    ax = plt.plot(eras, error_list)
    plt.show()


    line1.set_ydata(error_list)
    line1.set_xdata(eras)
    figure.canvas.draw()
    figure.canvas.flush_events()

    x = y
    y = y+1
    sleep(0.5)