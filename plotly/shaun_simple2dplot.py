# Simple 2d plot - shaun bowman, 08/28

import numpy as np # numpy
import matplotlib.pyplot as plt

def sinus2d(x, y):
    local_val = np.sin(x) + np.sin(y)
    return local_val 

x = y = np.arange(-2*np.pi, 2*np.pi, np.pi/50)
X, Y = np.meshgrid(x, y)

Z = sinus2d(X,Y)

plt.imshow(Z, origin='lower', interpolation='none')
plt.show()
