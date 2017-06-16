import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

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
    return

def trapezoid(pars,t):
    f = np.zeros(len(t))
    t0, T, tau, depth = pars
    int = (t > (t0 - T/2)) & (t <= (t0 - T/2 + tau))
    inf = (-(t - t0 + T/2) * depth/tau)
    mid = (t >  t0 - T/2 + tau) & (t <= t0 + T/2 - tau)
    out = (t >  t0 + T/2 - tau) & (t <= t0 + T/2)
    outf= ((t - t0 - T/2) * depth/tau)
    
    return inf * int - mid * depth + out * outf

def vary_depth(depths):
    for i in depths:
        pars = [0, 1.0, 0.2, i]
        t=np.linspace(-2,2,1000)
        plt.plot(t, trapezoid(pars,t))
    plt.ylim(-2017,50)
    return

def vary_duration(durations):
    for T in durations:
        pars = [0, T, 0.2, 200]
        t = np.linspace(-2,2,1000)
        plt.plot(t, trapezoid(pars,t))
    plt.ylim(-250, 50)
    return
 
def vary_tau(taus):
    for i in taus:
        pars = [0, 1.0, i, 200]
        t = np.linspace(-2,2,1000)
        plt.plot(t, trapezoid(pars,t))
    plt.ylim(-250,50)
    return

def vary_t0(t0s):
    for i in t0s:
        pars = [i, 1.0, 0.2, 200]
        t = np.linspace(-2,2,1000)
        plt.plot(t, trapezoid(pars,t))
    plt.ylim(-250,50)
    return

def plot_fit(7016.01, param_guess):
    t,f = tr.read_data(7016.01)
    plt.ylim(-600, 600)

    fig = plt.figure(figsize=(6, 4))
    fig.text(0.5, 0.04, "Time from mid-transit [days]", ha='center')
    fig.text(0.04, 0.5, 'Relative Flux', va='center', rotation='vertical')

    sub1 = fig.add_subplot(221) 
    trap1 = trapezoid(param_guess, t)
    sub1.scatter(t, f)
    sub1.plot(t, trap1)

    newf = f - f2

    sub2 = fig.add_subplot(222)
    sub2.scatter(t, newf)

    trap2 = np.zeros(len(t))
    sub2.plot(t, trap2)

    return

def chisqr(pars):
    t, y1 = read_data(7016.01)
    y2 = trapezoid(pars, t)
    return np.sum((y1-y2)**2)

def fit_trapezoid(data_num, method = 'Nelder-Mead'):
    val = minimize(chisqr, [0, 0.8, 0.2, 200], method=method)
    del val['final_simplex']
    return val
