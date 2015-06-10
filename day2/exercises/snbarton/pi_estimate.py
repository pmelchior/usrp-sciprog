#S. Nicholas Barton, pi_estimate.py, 10th June 2015

#estimates pi using a Monte Carlo method of throwing darts
#in order to do this we compare number of 'darts' inside 
#a unit circle inscribed within a square and take a ratio
#such that pi ~ 4 * (Number of darts in circle)/(Number of darts in square)


import numpy as np
import matplotlib.pyplot as plt

def generate_darts(size):
	"""
	Returns specified number of [x,y] coordinate pair(s) between -1 and 1
	"""
	x = 2 * np.random.random(size) - 1
	y = 2 * np.random.random(size) - 1
	return x,y

def is_in_circle(dart):


print(generate_darts(100))