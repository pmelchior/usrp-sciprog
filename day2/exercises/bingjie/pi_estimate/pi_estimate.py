#!/usr/bin/env python
# coding: utf-8

import numpy as np
from time import clock
import matplotlib.pyplot as plt

class MC(object):
    '''
    A class to do various things to estimate pi, using MC.
    '''
    
    # Class variables
    global Asq 
    Asq = 4.
    
    global xx_list
    global yx_list
    
    def __init__(self, N, time):
        '''
        Initialization. 
        N: number of points. 
        time: if True, returns the time used for the calculation.
        '''
        self.N = N
        self.time = time
        
    def pi(self):
        '''
        estimate pi using MC
        '''
        start = clock()
        count = 0.
        for i in xrange(int(self.N)):
            x = np.random.rand(2.) # 2 dim
            y = np.sum(x**2.)
            if y<=1.:
                count += 1.
            
        I = Asq*count/self.N
        end = clock()
        #print I
        #time = end - start
        if self.time is True:
            #print 'time used:', end - start, 's.'
            return [I, end - start]
        else:
            return I

    def darts(self):
        #two lists do not share same length..weird
        xx_list = []
        yx_list = []
        for i in xrange(int(self.N)):
            x = np.random.rand(2.)
            y = np.sum(x**2.)
            if y<=1.:
                xx_list.append(x[0])
                yx_list.append(x[1])
        return xx_list, yx_list




