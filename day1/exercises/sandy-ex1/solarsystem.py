import numpy as np

class Star:

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
	def __str__(self):
		return ""

half_sun = Star(mass=0.5, radius=0.5, name='Demisol')
print half_sun.name