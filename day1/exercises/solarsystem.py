class Star(object):
    def __init__(self, mass=1.0, radius=1.0, name='Sol'):
        """
        Takes inputs mass, radius, name
        """
        self.mass = mass
        self.radius = radius
        self.name = name

    def __str__(self):
        return '{}: {:.2f} M_sun, {:.2f} R_sun'.format(self.name, self.mass, 
            self.radius)
 
class Planet(object):
    def __init__(self,period,radius,name,mass=None):
        """
        Takes inputs period, radius, name, mass
        """
        self.period = period
        if mass is None:
            self.mass = radius**2
        else: self.mass = mass
        self.radius = radius
        self.name = name
    
    def __str__(self):
        return '{}: {:.0f} days, {:.2f} R_earth, {:.2f} M_earth, \
density = {:.1f} g/cc'.format(self.name,self.period,self.radius,
            self.mass,self.density)
    
    @property
    def density(self):
        return 5.51 * self.mass / self.radius**3

class System(object):
    def __init__(self,star,planets):
        """
        Takes a Star object and a list of Planet objects and creates
        a System object
        """
        self.star = star
        self.planets = planets

    def __str__(self):
        return '{}: {:.2f} M_sun, {:.2f} R_sun'.format(self.star.name, self.star.mass, 
            self.star.radius)

    def n_planets(self):
        return len(self.planets)

    def add_planet(self,planet):
        self.planets = self.planets.append(planet)


sun = Star()
half_sun = Star(mass=0.5, radius=0.5, name='Demisol')
earth = Planet(365, 1.0, mass=1.0, name='Earth')
venus = Planet(226, 0.92, name='Venus')