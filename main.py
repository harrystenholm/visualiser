import matplotlib.pyplot as plt
import numpy as np

x1=-10
x2=10
y1=-10
y2=10

fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])

plt.show()