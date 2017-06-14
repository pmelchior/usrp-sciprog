#! /Users/cnstahl/anaconda3/bin/python

import numpy as np

array = np.zeros((16,64))

array[1, :] += 1
for i in range(2,16):
    array[i] = array[i-1] + array[i-2]

mask = (array[:,0] % 2 == 0)
print(array[mask,:])
