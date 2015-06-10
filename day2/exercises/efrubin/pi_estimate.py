#!/usr/bin/env python
import numpy as np
import sys

class Darts(n):
	'''a class to calculate pi using monte carlo methods and time the calculation'''
	def __init__(self):

	def monte_carlo(n):
		'''generates n (x,y) points and checks if they fall within the unit circle'''
		n=int(n)
		pairs = np.random.rand(n,2) #generates n pairs of numbers

		accumulator = 0.0

		for i in range(n):
			if pairs[i][0]**2 + pairs[i][1]**2 <1:
				accumulator +=1

		pi_guess = (4*accumulator)/n

		return pi_guess

	
if __name__ == '__main__':
	print Darts.monte_carlo(sys.argv[1])