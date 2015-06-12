import singleTest as sT
import numpy as np
import time
import matplotlib.pyplot as pl
from matplotlib import rc, rcParams
rcParams.update({'font.size': 20})
#set up tex interpreter
rc('text',usetex=True)

class multiTest(object):
	"""
	doing multi test tasks for pi estimate
	"""

	def __init__(self, Nlist):
		self.Nlist = np.array(Nlist)
		timelist = []
		pilist = []

		for N in self.Nlist:
			newtest = sT.singleTest(N)
			new_pi = newtest.estimate()
			new_t = newtest.time_estimate()
			timelist += [new_t]
			pilist += [new_pi]

		self.tlist = np.array(timelist)
		self.pilist = np.array(pilist)

	def plottime_N(self):

		pl.figure()
		pl.clf()
		pl.hold(True)
		pl.plot(self.Nlist, self.tlist, 'r-.')
		pl.xlabel('N')
		pl.ylabel('t (s)')
		pl.xscale('log')
		pl.show()

	def plotprecision_N(self):

		pl.figure()
		pl.clf()
		pl.hold(True)
		pl.plot(self.Nlist, self.pilist - np.pi, 'r-.')
		pl.xlabel('N')
		pl.ylabel('pi(calc) - pi')
		pl.xscale('log')
		pl.show()