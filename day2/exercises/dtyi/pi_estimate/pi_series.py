#!/usr/bin/env python
import numpy as np
import time
import pi_estimate.estimator as es

class Pi_Series(object):

	def __init__(self,mincount,maxcount=None,runs=1):
		self.runs = runs
		self.mincount = mincount
		self.maxcount = maxcount

		if maxcount is None:
			self.maxcount = mincount

		self.counts, self.estims, self.times = [],[],[]

		geom_series = np.linspace(
			np.log(self.mincount),np.log(self.maxcount),runs)

		for n in np.round(np.exp(geom_series)).astype(int):

		    self.counts.append(n)
		    #print "n="+str(self.counts[-1]).ljust(9),
		    
		    start_time = time.time()
		    
		    self.estims.append(es.pi_estimator(n).estimate)
		    #print str(self.estims[-1]).ljust(8),    
		    
		    self.times.append((time.time()-start_time))
		    #print "%.4f seconds" %self.times[-1]

	def __str__(self):
		string_rep = ""
		for run in range(self.runs):
			string_rep += "n="+str(self.counts[run]).ljust(9)
			string_rep += str(self.estims[run]).ljust(13)
			string_rep += " %.4f seconds" %self.times[run] + "\n"
		return string_rep