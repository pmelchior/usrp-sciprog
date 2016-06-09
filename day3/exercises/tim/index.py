import numpy as np

nrows = 6
ncols = 3

arr = np.zeros((nrows,ncols))

for i in range(nrows):
    for j in range(ncols):
        arr[i,j] = i+j

print(arr)