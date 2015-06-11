#!/usr/bin/env python
import random
import time
import matplotlib.pyplot as plt
import math
import pylab as py

class PiGen:

    def __init__(self, N = 0):
        '''initialize PiGen, estimate pi and record points and time elapsed'''
        self.sample = N
        start = time.time()
        circle_count = 0.0
        total_count = 0.0
        points = []
        for i in xrange(0, N):
            x, y = random.random(), random.random()
            total_count += 1
            points.append([x, y])
            if (x**2 + y**2) < 1:
                circle_count += 1

        piEst = (circle_count / total_count) * 4
        end = time.time()
        time_elapsed = end - start

        self.pi = piEst
        self.points = points
        self.time = time_elapsed

    def plot_points(self):
        '''plot points used for pi approximation'''
        x_coordinates = [point[0] for point in self.points]
        y_coordinates = [point[1] for point in self.points]
        plt.plot(x_coordinates, y_coordinates, 'ro')
        plt.show()

class MultiPiGen:

    def __init__(self, samples = []):
        '''calculate pi estimates for multiple sample sizes'''
        self.sample_list = samples
        self.pi_list = []
        self.time_list = []
        for size in samples:
            temp = PiGen(size)
            self.pi_list.append(temp.pi)
            self.time_list.append(temp.time)

    def plot_times(self):
        '''plot times elapsed for pi approximations against sample sizes'''
        plt.plot(self.sample_list, self.time_list, 'ro')
        plt.show()

    def plot_estimates(self):
        '''plot pi approximations against sample sizes'''
        plt.plot(self.sample_list, self.pi_list, 'ro')
        plt.axhline(y = math.pi)
        plt.show()

class ManyPiGen:

    def __init__(self, N = 0, iterations = 0):
        '''calculate pi estimates muiple times for one sample size'''
        self.sample = N
        self.iter = iterations
        self.pi_list = []
        for i in xrange(0, iterations):
            temp = PiGen(N)
            self.pi_list.append(temp.pi)

        total = 0
        for estimate in self.pi_list:
            total += estimate

        self.mean = total / iterations

        sumsquares = 0
        for estimate in self.pi_list:
            sumsquares = (estimate - self.mean)**2

        self.stdev = math.sqrt(sumsquares / iterations)

    def plot_histogram(self):
        '''plot histogram of pi estimates for given sample size'''
        numBins = math.sqrt(self.iter)
        plt.hist(self.pi_list, numBins)
        plt.show()




