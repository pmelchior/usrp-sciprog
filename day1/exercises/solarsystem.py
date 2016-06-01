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
        self.density = 5.51 * self.mass / self.radius**3
        self.name = name
    
    def __str__(self):
        return '{}: {:.0f} days, {:.2f} R_earth, {:.2f} M_earth, \
density = {:.1f} g/cc'.format(self.name,self.period,self.radius,
            self.mass,self.density)

    def __setattr__(self,name,value):
        self.__dict__[name] = value
        if (self.__dict__[name] != None) and ((name == 'mass') or (name == 'radius')):
            self.__dict__[name] = value
            self.density = 5.51 * self.mass / self.radius**3

earth = Planet(365,1.0,mass = 1.0, name = "Earth")
print(earth)
venus = Planet(226,0.92,name="Venus")
print(venus)
print venus.mass, venus.density
venus.mass = 0.81
print venus.mass, venus.density
