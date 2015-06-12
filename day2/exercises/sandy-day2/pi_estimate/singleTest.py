import numpy as np
import time
import matplotlib.pyplot as pl
from matplotlib import rc, rcParams
rcParams.update({'font.size': 20})
#set up tex interpreter
rc('text',usetex=True)

class singleTest(object):
	"""
	single estimate of pi value, with time or not, with plot or not
	"""

	def __init__(self, N):

		start = time.time()

		self.N = N

		self.in_count = 0

		self.xlist = []
		self.ylist = []

		for i in range(0, self.N):
			new_x = np.random.rand()
			new_y = np.random.rand()
			self.xlist += [new_x]
			self.ylist += [new_y]

			dist = np.sqrt((new_x - 0.5)**2 + (new_y - 0.5)**2)

			if dist < 0.5:
				self.in_count += 1

		end = time.time()

		self.time = end - start

	def estimate(self):

		return float(self.in_count)/self.N*4


	def time_estimate(self):

		return self.time

	def dartplot(self):

		pl.figure()
		pl.clf()
		pl.hold(True)
		pl.title('N = ' + str(self.N))
		pl.plot(self.xlist, self.ylist, 'r+')
		param = np.linspace(0,1,num=1000)
		xc = 0.5 + 0.5*np.cos(np.pi*2*param)
		yc = 0.5 + 0.5*np.sin(np.pi*2*param)
		pl.plot(xc, yc, 'b-')
		pl.xlabel('x')
		pl.ylabel('y')
		pl.xlim(0,1)
		pl.ylim(0,1)
		pl.show()

	

"""
print estimate(100)
print estimate(1000)
print estimate(10000)
print estimate(1e6)
"""

#[pi, t] = time_estimate(1000, plotdart = True)
#print pi, t

"""
Nlist = np.logspace(1, 5, num=20).astype(int)
timelist = []

for n in Nlist:
	[new_pi, new_t] = time_estimate(n)

	timelist = timelist + [new_t]

timelist = np.array(timelist)

pl.figure(1)
pl.clf()
pl.hold(True)
pl.plot(Nlist, timelist, 'r-.')
pl.xlabel('N')
pl.ylabel('t (s)')
pl.xscale('log')
pl.show()
"""


