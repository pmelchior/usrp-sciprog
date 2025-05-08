%matplotlib inline
import numpy as np
import scipy.optimize as so
import matplotlib.pyplot as plt

result = so.minimize_scalar(f, bracket=(-10,10))
x = np.linspace(-10,10,100)
plt.plot(x, f(x))
plt.scatter([result.x], [result.fun], c='r',zorder=10)
