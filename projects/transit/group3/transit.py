import numpy as np
import matplotlib.pyplot as plt

def read_data(ob_num):
    with open('../data/'+str(ob_num)+'.txt') as f: 
        data= np.loadtxt(f, dtype=float)
    t=data[:,0]
    f=data[:,1]
    return(t,f)
    pass

def plot_data():
    pass

def trapezoid():
    pass

def vary_depth():
    pass

def vary_duration():
    pass

def vary_tau():
    pass

def vary_t0():
    pass

def plot_fit():
    pass

def fit_trapezoid():
    pass

