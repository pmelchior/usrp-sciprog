#! /usr/bin/env python

import numpy as np

class Darts:
    def __init__(self, n_darts = 10, x_min = -1, x_max = 1, y_min = -1, y_max = 1):
        n_darts = int(n_darts)
        y = np.random.uniform(y_min, y_max, n_darts)
        x = np.random.uniform(x_min, x_max, n_darts)
        self.darts = np.vstack((x, y))

    def estimate_pi(self):
        dists = np.sqrt(self.darts[0] * self.darts[0] + self.darts[1] * self.darts[1])
        incir = dists < 1
        return np.sum(incir)/len(incir)*4
