import numpy as np
import matplotlib.pyplot as plt

def read_data(ob_num):
    with open('../data/'+str(ob_num)+'.txt') as f: 
        data= np.loadtxt(f, dtype=float)
    t=data[:,0]
    f=data[:,1]
    return(t,f)

def plot_data(ob_num):
    with open('../data/'+str(ob_num)+'.txt') as f: 
        data= np.loadtxt(f, dtype=float)
    t=data[:,0]
    f=data[:,1]
    plt.scatter(t,f)
    plt.xlabel('Time from the mid-transit [days]')
    plt.ylabel('Relative Flux [PPM]')
    pass

def trapezoid(pars, t):
    f = np.zeros(len(t))
    t0, T, tau, depth = pars
    int = (t > (t0 - T/2)) & (t <= (t0 - T/2 + tau))
    inf = (-(t - t0 + T/2) * depth/tau)
    mid = (t >  t0 - T/2 + tau) & (t <= t0 + T/2 - tau)
    out = (t >  t0 + T/2 - tau) & (t <= t0 + T/2)
    outf= ((t - t0 - T/2) * depth/tau)
    
    return inf * int - mid * depth + out * outf

def vary_depth():
    pass

def vary_duration(durations):
    for T in durations:
        pars = [0, T, 0.2, 200]
        t = np.linspace(-2,2)
        plt.plot(t, trapezoid(pars,t))
    plt.ylim(-250, 50)
    return
 
def vary_tau():
    pass

def vary_t0():
    pass

def plot_fit():
    pass

def fit_trapezoid():
    pass

