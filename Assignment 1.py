# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt


#generate and plot the sine and cosine functions using numpy and matplotlib:

x = np.arange(-2*np.pi, 2*np.pi + 0.1, 0.1)

y_one = np.sin(x)

y_two = np.cos(x)


plt.plot(x, y_one, label = 'Sine')
plt.plot(x, y_two, label = 'Cosine')
plt.xlim([-5,5])
plt.xticks([-2*np.pi, -1*np.pi, 0, np.pi, 2*np.pi], labels = 
           ['-2Pi', '-Pi', '0', 'Pi', '2Pi'])
plt.legend()
plt.show()

