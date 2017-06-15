import matplotlib.pyplot as plt
import numpy as np 

A = np.random.uniform(0, 1, size=8)
ω = np.random.uniform(-np.pi, np.pi, size=8)

t = np.linspace(0, 32, 1024)

f = A[np.newaxis] * np.cos(ω[np.newaxis]*t[:,np.newaxis])
print(A[np.newaxis].shape)
print(ω[np.newaxis].shape)
print(t[:,np.newaxis].shape)
print(f.shape)

f = np.sum(f, axis=1)
print(f.shape)

plt.plot(t, f)
plt.show()
