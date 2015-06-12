#!/usr/bin/env python
import numpy as np

class Pi_Estimator:
	"""
	Makes a sample of n points in a unit square,
	and checks which ones lie within a unit circle,
	estimating pi as 4* that proportion.
	"""
	def __init__(self, n):

		self.tosses = np.random.random_sample((n,2))
		self.within = 0

		for i in range(n):
			if self.tosses[i][0]**2+self.tosses[i][1]**2 < 1:
				self.within+=1

		self.estimate = 4*self.within/float(n)
		# or: from __future__ import division


