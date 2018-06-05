import numpy as np

a = np.random.uniform(2,17, 100).astype(int)
a = a[np.logical_and(a > 5, a < 10)]
a= a[a%2==0]

print(a)
