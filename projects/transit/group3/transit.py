import numpy as np
import matplotlib.pyplot as plt

def read_data(ob_num):
    with open('../data/'+str(ob_num)+'.txt') as f: 
        data= np.loadtxt(f, dtype=float)
    t=data[:,0]
    f=data[:,1]
    return(t,f)

def plot_data():
    pass

def trapezoid(pars, t):
    f = np.zeros(len(t))
    t0, T, tau, depth = pars
    ins = (t > (t0 - T/2)) & (t <= (t0 - T/2 + tau))
    ins = -ins * (t - t0 + T/2) * depth/tau

    return f + ins

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

