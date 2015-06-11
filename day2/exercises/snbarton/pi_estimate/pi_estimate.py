#S. Nicholas Barton, pi_estimate.py, 10th June 2015

#estimates pi using a Monte Carlo method of throwing darts
#in order to do this we compare number of 'darts' inside 
#a unit circle inscribed within a square and take a ratio
#such that pi ~ 4 * (Number of darts in circle)/(Number of darts in square)


import numpy as np
import matplotlib.pyplot as plt
import math
import time

def generate_darts(size):
	"""
	Returns a specified number of [x,y] coordinate pairs in the range [-1,1)
	"""
	x = 2 * np.random.random(size) - 1
	y = 2 * np.random.random(size) - 1
	return x,y

def is_in_circle(dart_x,dart_y):
	"""
	Returns whether a dart lands in the unit circle
	"""
	return (math.sqrt(dart_x**2 + dart_y**2) <= 1)

def draw_circle(r,phi):
	return r*np.cos(phi), r*np.sin(phi)


number = [100,1000,10000,1000000]

plots = np.empty([len(number),3])
for i,n in enumerate(number):
	#print i,n
	start = time.time()
	darts_x, darts_y = generate_darts(n)
	#print darts_x, darts_y
	counter = 0
	for j in range(n):
		if is_in_circle(darts_x[j],darts_y[j]):
			counter += 1
			continue

	plots[i,0] = 4*counter/float(n)
	end = time.time()
	plots[i,1] = end - start
	plots[i,2] = math.pi - plots[i,0]

phis = np.arange(0,6.28,0.01)
r=1

plt.figure(1)
plt.plot(number,plots[:,1])
plt.xlabel('Number of darts')
plt.ylabel('Calculation time in seconds')
plt.title('Runtime of pi_estimate.py')

# plt.xlim(-1,1)
# plt.ylim(-1,1)
# plt.plot(darts_x,darts_y,c='k',',')
# plt.plot(*draw_circle(r,phis),c='k',ls='-')
# plt.show()

