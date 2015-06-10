import numpy as np

class Star:
	def __init__(self):
		self.m = 1
		self.r = 1
		self.n = 'sun'
	def __init__(self, mass, radius, name):
		self.m = mass
		self.r = radius
		self.n = name
	def __str__(self):
		return self.n + ": mass = " + str(self.m) + " M_sun, radius = " + str(self.r) + " R_sun."

half_sun = Star()
print(half_sun)