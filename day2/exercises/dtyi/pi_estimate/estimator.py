#!/usr/bin/env python
import numpy as np

class pi_estimator:

	def __init__(self, n):
		tosses = np.random.random_sample((n,2))
		self.within = 0

		for i in range(n):
			if tosses[i][0]**2+tosses[i][1]**2 < 1:
				self.within+=1

		self.estimate = 4*self.within/float(n)
		# or: from __future__ import division


