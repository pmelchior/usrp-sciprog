from math import pi

class Star(object):
    def __init__(self, mass=1.0, radius=1.0, name='Sol'):
        """
        Takes inputs mass, radius, name
        """
        self.mass = mass
        self.radius = radius
        self.name = name

    def __str__(self):
        return '{}: {:.2f} M_sun, {:2f} R_sun'.format(self.name, self.mass, self.radius)
 
class Planet(object):
    def __init__(self,period,radius,name,mass=radius**2):
        """
        Takes inputs period, radius, name, mass
        """
        self.period = period
        self.mass = mass
        self.radius = radius
        self.density = self.mass / (4/3 * pi * self.radius**3)
        self.name = name
    
    def __str__(self):
        return '{:0f}: {:2f} days, {:2f} R_earth, {:2f} M_earth, + \
        density = {:1f} g/cc'.format(self.name,self.period,self.radius,self.mass)

sun = Star()
print(sun)
