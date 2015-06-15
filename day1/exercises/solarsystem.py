import string
class Star(object):
    def __init__(self,name="Sun",mass=1.,radius=1.):
    	self.name = name
    	self.mass = mass
    	self.radius = radius
    def __str__(self):
    	return "{}:{} M_sun, {} R_sun".format(self.name,self.mass,self.radius)
class Planet(object):
    def __init__(self,day,radius, name="Earth",mass=1.):
    	self.day = day
    	self.name = name
    	self.mass = mass
    	self.radius = radius
    	self.density=mass*5.97219e27/(4./3.*3.14*(637810000*radius)**3) #5.97219e27 convert M_sun to g
    def __str__(self):
    	return "{}: {} days, {} R_earth, {} M_sun, density = {} g/cc".format(self.name, self.day, self.radius,self.mass,self.density)

class System(object):
    def __init__(self,star, planets):
    	self.star=star #Name of the central star
    	self.planets=planets
    	self.n_planets=len(planets)
    def add_planet(self,new_planet):
    	if (new_planet.name=="Earth"): #Default, no provided
    		new_planet.name="Demisol"
    	suffix = ""
    	alphabets = list(string.ascii_lowercase)
    	#n = --- contain Demisol
    	
    	for i in self.planets:
    		if i.name==	"Earth":
    			suffix="-"+alphabets[n]
    	self.planets.append(new_planet)
    	self.n_planets+=1
    def __getitem__(self,idx):
    	for i in self.planets:
    		if i.name ==idx:
    			return i


    def __str__(self):
    	print  "Sol: {} M_sun, {} R_sun".format(self.star.mass,self.star.radius)
    	for i in self.planets: 
    		print i
    	return ""

