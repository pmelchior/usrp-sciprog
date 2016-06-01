#!/usr/bin/env python
import time
from pi_calc import darts

def timer(n):
	'''finds the time for calculating pi using monte_carlo given the number of points'''
	start = time.time()
	pi_estimate = darts(n)
	end = time.time()
	elapsed = end - start

	return elapsed