#!/usr/bin/env python
import numpy as np
import sys

def darts(n):
	'''generates n (x,y) points and checks if they fall within the unit circle'''
	n=int(n)
	pairs = np.random.rand(n,2) #generates n pairs of numbers

	accumulator = 0

	for i in range(n):
		if pairs[i][0]**2 + pairs[i][1]**2 <1:
			accumulator +=1

	pi_guess = (4.*accumulator)/n

	return pi_guess

	
if __name__ == '__main__':
	print darts(sys.argv[1])