class Star(object):
	def __init__(self, mass=1.0, radius=1.0, name='Sol'):
		self.mass = mass
		self.radius = radius
		self.name = name

	def __str__(self):
		print('{}: {} M_sun, {} R_sun'.format(self.name,self.mass,self.radius))

sun = Star()
