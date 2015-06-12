
# coding: utf-8

# In[18]:

class Star:
    def __init__(self, mass=1.00, radius=1.00, name='sol'):
        self.mass = mass
        self.radius = radius
        self.name = name
    def __str__(self):
        return '%s: %03.2f M_sun, %03.2f R_sun' % (self.name, self.mass, self.radius)
        


# In[170]:

class Planet:
    def __init__(self, days_per_year=365, radius=1, name='Earth', mass = 'a'):
        self.days_per_year = days_per_year
        self.radius = radius
        self.name = name
        if (mass == 'a'):
            self.mass = radius**2.
        else:
            self.mass = mass
        self.density = 5.51 * self.mass / (self.radius)**3.
    def __str__(self):
        return '%s:%03.2f days, %03.2f R_earth, %03.2f M_earth, density = %f g/cc' % (self.name, self.days_per_year, self.radius, self.mass, self.density)


# In[171]:

class System:
    def __init__(self, star, planets):
        self.star = star
        self.planets = planets
        self.n_planets = len(planets)
    def add_planet(self, new):
        self.planets.append(new)
        self.n_planets+=1
    def __str__(self):
        print "{}: {} M_sun, {} R_sun" .format(self.star.name, self.star.mass, self.star.radius)
        for i in self.planets:
            print i
        return ' '


# In[ ]:




# In[ ]:




# In[ ]:



