import numpy as np

arr1 = np.ones([4,4])
arr1[2,3] = 2
arr1[3,1] = 6
print(arr1.astype(int))

arr2 = np.zeros([5,5])
for i in range(len(arr2)):
    arr2[i,i] = i + 1
print(arr2)
