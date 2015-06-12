import numpy as np
import string
alphab = string.ascii_lowercase

class Star:

	def __init__(self, **kwargs): 
		if len(kwargs) == 0:
			self.__dict__.update(name = 'sun')
			self.__dict__.update(mass = 1)
			self.__dict__.update(radius = 1)
		else:
			self.__dict__.update(kwargs)
	def __str__(self):
		return "{}: mass = {} M_sun, radius = {} R_sun".format(self.name, str(self.mass), str(self.radius))


class Planet:

	def __init__(self, *args, **kwargs):
		self.period = args[0]
		self.radius = args[1]
		self.__dict__.update(kwargs)
		if not hasattr(self, 'mass'):
			self.mass = self.radius**2
		if not hasattr(self, 'name'):
			self.name = ""

	@property
	def density(self):
		return self.mass/self.radius**3*5.5

	def __str__(self):
		return "{}: {} days, {} R_earth, {} M_earth, density = {} g/cc"\
		.format(self.name, str(self.period), str(self.radius), str(self.mass), str(self.density))

class System:

	def __init__(self, star, **kwargs):
		self.star = star
		self.__dict__.update(kwargs)
		if len(kwargs) == 0:
			self.planets = []

	def __str__(self):
		str_final = self.star.__str__() + "\n"
		i = 1
		for planet in self.planets:
			if planet.name == "":
				planet.name = self.star.name + " " + alphab[i-1]
			new_string = "  " + planet.__str__() + "\n"
			str_final = str_final + new_string
			i = i + 1
		return str_final

	@property
	def n_planets(self):
		return len(self.planets)

	def add_planet(self, planet):
		self.planets = self.planets + [planet]

sun = Star()
print(sun)
half_sun = Star(mass=0.5, radius=0.5, name='Demisol')
print(half_sun)
earth = Planet(365, 1.0, mass=1.0, name='Earth')
print(earth)
venus = Planet(226, 0.92, name='Venus') #if mass not provided, use M = R^2
print(venus)
venus.mass = 0.81 #Venus's actual 
print venus.mass
print venus.density
ss = System(sun, planets=[earth, venus])
print ss.n_planets
mercury = Planet(88, 0.38, name='Mercury')
ss.add_planet(mercury)
print ss.n_planets
print(ss)
ss2 = System(half_sun)
ss2.add_planet(Planet(44, 0.19))
ss2.add_planet(Planet(182, 0.5))
ss2.add_planet(Planet(113, 0.46))
print(ss2)