'''
uses pi_estimate/board.py to generate statistics on the results of calculating pi statistically
'''

import board
import matplotlib.pyplot as plt
import genpoint
import checkpoint
import numpy as np


def testn(n, k):
   ''' 
   gens k boards of n points and uses them to calculate calculate pi k times, and plots the resulting values in a histogram 
   '''
   pi_ests = [];
   for i in range(0, k):
      b = board.Board(n);
      pi_ests.append(b.calculate_pi());
   print len(pi_ests)
   plt.figure()
   plt.hist(pi_ests, 30)
   plt.ylabel('frequency')
   plt.xlabel('estimated pi value using {} points/board'.format(n))
   plt.savefig('/Users/evematthaey/repositories/usrp-sciprog/day2/exercises/evematthaey/pi_estimate/pivaluehist_{}_{}.png'.format(n, k))
   plt.close()


def accuracy():
   ''' 
   generates boards of sizes varying between 100 and 1e6 and plots the accuracy of their pi estimates 
   '''
   num_points = []
   pi_errs = []
   for i in range(0, 40):
        num_points.append(100 * 1.2589**i)
        b = Board(num_points[i])
        pi_errs.append(b.calculate_pi() - np.pi);

   plt.figure()
   plt.semilogx(num_points, pi_errs)
   plt.xlabel('log number of points on board')
   plt.ylabel('error on pi measurement')
   plt.savefig('pi_errors.png')
   plt.close()


