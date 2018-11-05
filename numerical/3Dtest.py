# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:05:40 2018

@author: ayana
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x = [-1, 1]
y = [-1, 1]
X, Y = np.meshgrid(x, y)
Z = np.array([[1, 1], [1, 1]])

ax = plt.subplot(111, projection='3d')
ax.plot_surface( X,  Y,  Z, alpha=0.7)
ax.plot_surface( X,  Y, -Z, alpha=0.7)
ax.plot_surface( X,  Z,  Y, alpha=0.7)
ax.plot_surface( X, -Z,  Y, alpha=0.7)
ax.plot_surface( Z,  X,  Y, alpha=0.7)
ax.plot_surface(-Z,  X,  Y, alpha=0.7)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
plt.show()
