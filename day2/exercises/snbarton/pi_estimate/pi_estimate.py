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
	Returns a specified number of [x,y] coordinate pairs in the \
	range [-1,1)
	"""
	x = 2 * np.random.random(size) - 1
	y = 2 * np.random.random(size) - 1
	return x,y

def is_in_circle(dart_x,dart_y):
	"""
	Returns whether a dart lands in the unit circle
	"""
	return (math.sqrt(dart_x**2 + dart_y**2) <= 1)

def throw_darts(number):
	"""
	Throws a specified number of darts and returns the number that landed \
	in the circle
	"""
	darts_x, darts_y = generate_darts(number)
	counter = 0
	for i in range(number):
		if is_in_circle(darts_x[i],darts_y[i]):
			counter +=1
			continue
	return counter

def draw_circle(r,phi):
	"""Converts radial coordinate pairs to Cartesian pairs
	"""
	return r*np.cos(phi), r*np.sin(phi)

#def plot_darts(number):






if __init__ == "__main__":

	# number = [100,1000,10000,1000000]

	# plots = np.empty([len(number),2])
	# for i,n in enumerate(number):
	# 	start = time.time()
	# 	counter = throw_darts(n)
	# 	plots[i,0] = 4*counter/float(n)
	# 	end = time.time()
	# 	plots[i,1] = end - start



	# plt.figure(1)
	# plt.plot(number,plots[:,1])
	# plt.xlabel('Number of darts')
	# plt.ylabel('Calculation time in seconds')
	# plt.title('Runtime of pi_estimate.py')


	# darts_x, darts_y = generate_darts(100)
	# phis = np.arange(0,6.28,0.01)
	# r=1

	# plt.figure(2)
	# plt.xlim(-1,1)
	# plt.ylim(-1,1)
	# plt.plot(darts_x,darts_y,'k.')
	# plt.plot(*draw_circle(r,phis),c='k',ls='-')
	# plt.title('Plot of dart location of 100 darts')
	# plt.show()

	N = 100
	trials = 30
	estimates = np.empty(trials)

	for i in range(trials):
		counter = throw_darts(N)
		estimates[i] = 4*counter/float(N)

	plt.figure(3)
	hist = np.histogram(estimates)
	plt.plot(estimates,hist)
	plt.show()

