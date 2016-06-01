#!/usr/bin/env python
import numpy as np
import sys
import time
import pylab as plt
class PiGuess:
	'''Generates an estimate for pi using a monte carlo method given the number of points to use'''
	def __init__(self,n):

		self.n=int(n)
		#self.pi=0
		#self.pairs=[]
		self.time=0
		self.darts()
	def darts(self):
		'''generates n (x,y) points and checks if they fall within the unit circle'''
		'''also includes timing'''

		start = time.time()
		pairs = np.random.rand(self.n,2) #generates n pairs of numbers
		self.pairs=pairs
		accumulator = 0

		for i in range(self.n):
			if pairs[i][0]**2 + pairs[i][1]**2 <1:
				accumulator +=1

		self.pi = (4.*accumulator)/self.n
		end = time.time()
		self.time = end - start

	def plot_pairs(self):
		'''plots each x,y pair'''
		x = [self.pairs[i][0] for i in range(self.n)]
		y = [self.pairs[i][1] for i in range(self.n)]
		plt.figure()
		plt.plot(x,y,'o')
		plt.show()

	#query methods

	def n(self):
		return self.n

	def pi(self):
		return self.pi

	def pairs(self):
		return self.pairs

	def time(self):
		return self.time

	def __str__(self):
		print 'Monte Carlo computation of pi using %f points' % \
		 (self.n)

class PiGuess_N:
	'''generates a list of pi values using monte carlo based on an input list of n values'''

	def __init__(self, n_list):
		'''saves pi values and time values for each computation in list form'''
		self.n_list = n_list
		self.pi_list =[]
		self.time_list=[]

		for i in range(len(n_list)):
			scratch = PiGuess(n_list[i])
			self.pi_list.append(scratch.pi)
			self.time_list.append(scratch.time)

	def plot_time(self):
		'''plots time versus number of points'''

		x = self.n_list
		y = self.time_list
		plt.figure()
		plt.semilogx(x,y, 'o')
		plt.title('')
		plt.xlabel('n')
		plt.ylabel('computation time')
		plt.show()

	def plot_precision(self):
		x = self.n_list
		y = [i - np.pi for i in self.pi_list]
		plt.figure()
		plt.semilogx(x,y,'o')
		plt.xlabel('n')
		plt.ylabel('pi estimate - pi')
		plt.show()

	#query methods

	def pi_list(self):
		return self.pi_list

	def time_list(self):
		return self.time_list

	def n_list(self):
		return self.n_list
class PiGuess_Single:
	'''generates many pi estimates at using the same number of darts and performs analysis thereof''' 
		
	def __init__(self, n, iterations):
		self.n = n
		self.iterations = iterations
		self.pi_list = []
		for i in range(iterations):
			scratch = PiGuess(n)
			self.pi_list.append(scratch.pi)
		self.mean = sum(self.pi_list)/iterations
		self.std = sum([(guess - self.mean)**2 for guess in self.pi_list])/iterations
	
	def histogram(self):
		plt.figure()
		plt.hist(self.pi_list, bins=int(np.sqrt(self.iterations)))
		plt.show()

	#query methods

	def n(self):
		return self.n

	def iterations(self):
		return self.iterations

	def pi_list(self):
		return self.pi_list

	def mean(self):
		return self.mean

	def std(self):
		return self.std

