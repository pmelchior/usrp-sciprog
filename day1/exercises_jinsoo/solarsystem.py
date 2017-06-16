import numpy as np

class Star(object):
    def __init__(self, mass=1.00, radius=1.00, name="Sol"):
        self.mass = mass
        self.radius = radius
        self.name = name
    def __str__(self):
        return self.name + ": " + str(self.mass) + " M_sun, " + str(self.radius) + " R_sun"

class Planet(object):
    def __init__(self, period, radius, name=None, mass=None):
        self.period = period
        self.radius = radius
        if (mass==None):
            self.mass = radius**2
        else:
            self.mass = mass
        self.name = name
        r_earth = 6.3714e8
        m_earth = 5.972e27
        self.density = (self.mass*m_earth)/((4*np.pi*(self.radius*r_earth)**3)/3)
    def __str__(self):
        return self.name + ": " + str(self.period) + " days, " + str(round(self.radius,2)) + " R_earth, " + str(round(self.mass,2)) + " M_earth, density = " + str(round(self.density,1)) + " g/cc"

class System(object):
    def __init__(self, sun, planets=[]):
        self.sun = sun
        self.planets = planets
        self.n_planets = len(self.planets)

    def add_planet(self, planet):
        if (planet.name==None):
            planet.name = self.sun.name + "-"

    def __str__(self):
        return self.sun.name + ": " + str(self.sun.mass) + " M_sun, " + str(self.sun.radius) + " R_sun\n"
