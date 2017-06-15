class Star:
    
    def __init__(self, mass = 1., radius = 1., name = 'Sol'):
        self.mass = mass
        self.radius = radius
        self.name = name

    def __str__(self):
        a = (self.name, self.mass, self.radius)
        return "%s: %4.2f M_sun, %4.2f R_sun"% a

class Planet:

    def __init__(self, year, radius, mass = None, name = 'Earth'):
        self.year = year
        self.radius = radius
        if mass == None: self.mass = radius**2
        else: self.mass = mass
        self.name = name
        
        self.volume = 4*3.14159*radius**3/3
        self.density = self.mass/self.volume*5.51/0.238733 

    def __str__(self):
        a = (self.name, self.year, self.radius, self.mass, self.density)
        return "%s: %3d days, %4.2f R_earth, %4.2f M_earth, density = %3.1f g/cc"% a

class System: 

    def __init__(self, star, planets):
        self.star = star
        self.planets = reversed(planets)
        self.n_planets = len(planets)
        
    def __str__(self):
        string = str(self.star)
        for planet in self.planets:
            string = string + '\n  ' + str(planet)
        return string

    def __getitem__(self, key):
        if key == self.star.name: return self.star
        for planet in self.planets:
            if key == planet.name: return self.planet

    def add_planet(self, planet):
        self.planets.append(planet)
        self.n_planets += 1
