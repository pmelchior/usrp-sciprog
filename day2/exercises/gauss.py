#!/usr/bin/env python

import numpy as np

def gaussian2D(x, y, mean, cov):
    x_var = x - mean[0]
    y_var = y - mean[1]

    vals = np.vstack((x_var, y_var))
    dot  = np.dot(np.linalg.inv(cov).T, vals)
    prod = dot * vals

    return np.sum(prod, axis = 0)
    
import matplotlib.pyplot as plt

x = np.arange(0.,10.,0.1)
y = np.arange(0.,10.,0.1)
x,y = np.meshgrid(x,y)
mean_xy = np.array([5.,4.])
cov = np.array([[1.,1.],
                [1.,2.]])**2.

f = gaussian2D(x.ravel(), y.ravel(), mean_xy, cov)
f.reshape(100,100)

plt.imshow(f.reshape(100,100))
plt.show()
plt.savefig('pic.pdf')
