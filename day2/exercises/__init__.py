
# coding: utf-8

# In[1]:


import numpy as np
from math import sqrt

def getPoints(numPoints):
	randArr = np.random.uniform(-1, 1, (numPoints, 2))

	mask=[]

	for i in range(0, numPoints):
		mask.append(distanceCheck(randArr[i][1],randArr[i][0]))

	return mask


def distanceCheck(x, y):
	distance = sqrt(x**2 + y**2)
	return distance < 1 # returns false if outside circle

def truCounter(numPoints):
	truArray = getPoints(numPoints)

	numTrue = 0

	for i in range(0, numPoints):
		if truArray[i] == True:
			numTrue = numTrue + 1
	return numTrue

def estimatePi(numPoints):
	truCount = truCounter(numPoints)
	return 4 * truCount / (numPoints)

print(estimatePi(10000))

    

