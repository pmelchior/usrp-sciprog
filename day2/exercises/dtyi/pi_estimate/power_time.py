#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from . import pi_series as ps

class Power_law_time(object):

	def __init__(self,min_n,max_n,factor):
		print 'testing1'
		orders = np.log(max_n/min_n)/np.log(factor)+1

		time_experiment = ps.Pi_Series(min_n,max_n,orders)

		A = np.vstack([np.log(time_experiment.counts), np.ones(len(time_experiment.counts))]).T
		m,c = np.linalg.lstsq(A, np.log(time_experiment.times))[0]

		plt.loglog(time_experiment.counts,time_experiment.times,'bo',label='Test runs')
		plt.loglog(time_experiment.counts,np.exp(m*np.log(time_experiment.counts)+c),'r-',label='power-law fit')
		plt.legend()
		plt.figtext(0.6,0.7,"exponent is %.2f"%m, fontsize = 12)
		print 'testing2'
		plt.ylabel('time, s')
		plt.xlabel('n')
		plt.show()
