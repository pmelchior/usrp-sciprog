#!/usr/bin/env python
import sys

class Star:

	def __init__(self, mass=1.00, radius=1.00, name="Sol"):
		self.mass = mass
		self.radius = radius
		self.name = name

	def __str__(self):
		return self.name + ": %.2f M_sun, %.2f R_sun" \
		% (self.mass, self.radius)



class Planet(object):

	DENSITY_EARTH = 5.51
	def __init__(self, period, radius, mass=None, name=""):
		self.period = period
		self.radius = radius
		if mass is None:
			self.mass = self.radius**2
		else:
			self.mass = mass
		#self.density = self.mass*Planet.DENSITY_EARTH/self.radius**3
		self.name = name

	def __str__(self):
		return self.name +              \
		": %d days," % self.period +    \
		" %.2f R_earth," % self.radius +\
		" %.2f M_earth," % self.mass +  \
		" density = %.1f g/cc" % (self.mass*Planet.DENSITY_EARTH/self.radius**3)

	#def __setmass__(self, mass, value):
		#self.__dict__[mass] = value
		#self.density = self.mass*Planet.DENSITY_EARTH/self.radius**3

	@property
	def density(self):
		"""
		Compute the density from mass~r^3
		"""
		return self.mass*Planet.DENSITY_EARTH/self.radius**3


	#def density(self):
	#	return self.mass*Planet.DENSITY_EARTH/self.radius**3


class System(object):

	def __init__(self, star, planets=[]):
		self.star = star
		self.planets = planets

	def add_planet(self, planet):
		"""
		Add a planet to a System's list of planets.
		"""
		self.planets.append(planet)
		if planet.name == "":
			numbername = self.star.name + "-" + chr(ord('a') + self.n_planets)
			print 'Planet does not have name, will be named '+numbername+'.'
			planet.name = numbername

	@property
	def n_planets(self):
		return len(self.planets)

	def __str__(self):
		str = self.star.__str__()
		orderedplanets = sorted(self.planets, key=lambda planet: planet.period)
		for planet in orderedplanets:
			str = str + "\n  " 
			str = str + planet.__str__()
		return str

	def __getitem__(self, key):
		#for planet in self.planets:
		#	if planet.name == key:
		#		return planet

		filteredlist = [planet for planet in self.planets if planet.name==key]
		return filteredlist[0]


	#def _nameMatches_(planet, key):
	#	if planet.name == key: return True
	#	else: return False


if __name__ == "__main__":
	print "Hello, world!"