import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

t0 = 0
T = 1.0
tau = 0.2
depth = 200

def read_data(object_num):
    data = np.genfromtxt("../data/" + str(object_num) + ".txt", dtype=None, names=True)
    time = data['time']
    flux = data['flux']
    return time, flux

def plot_data(obj_n):
    t, f = read_data(obj_n)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(t,f)
    ax.set_xlabel('Time')
    ax.set_ylabel('Flux')
    plt.show()
    return

def trapezoid(pars, t):
    t0 = pars[0] #center time
    T = pars[1] #duration
    tau = pars[2] #ingress duration
    depth = pars[3] #depth
    m = depth/tau #slope

    t1 = t0 - T/2
    t2 = t0 - T/2 + tau
    t3 = t0 + T/2 - tau
    t4 = t0 + T/2

    return np.piecewise(t, [t < t1, t >= t1, t >= t2, t >= t3, t >= t4], [0, lambda t: -m*(t-t1), -depth, lambda t: m*(t-t4), 0])

def vary_depth(depths):
    t = np.linspace(-2.0,2.0,500)
    trap_list = [trapezoid((t0,T,tau, d), t) for d in depths]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-2.0,2.0)
    ax.set_ylim(-2050,50)
    for i in range(len(trap_list)):
        ax.plot(t, trap_list[i])
    plt.show()
    return

def vary_duration(durs):
    t = np.linspace(-2.0,2.0,500)
    trap_list = [trapezoid((t0, dur, tau, depth), t) for dur in durs]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-2.0,2.0)
    ax.set_ylim(-250,50)
    for i in range(len(trap_list)):
        ax.plot(t, trap_list[i])
    plt.show()
    return

def vary_tau(taus):
    t = np.linspace(-2.0,2.0,500)
    trap_list = [trapezoid((t0, T, x, depth), t) for x in taus]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-2.0,2.0)
    ax.set_ylim(-250,50)
    for i in range(len(trap_list)):
        ax.plot(t, trap_list[i])
    plt.show()
    return

def vary_t0(t0s):
    t = np.linspace(-2.0,2.0,500)
    trap_list = [trapezoid((x, T, tau, depth), t) for x in t0s]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-2.0,2.0)
    ax.set_ylim(-250,50)
    for i in range(len(trap_list)):
        ax.plot(t, trap_list[i])
    plt.show()
    return

def plot_fit(obj_num, pars_guess):
    t, f = read_data(obj_num)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(t,f, color='k')
    ax.plot(t, trapezoid(pars_guess,t),'r-')
    ax.set_xlabel('Time from mid-transit [days]')
    ax.set_ylabel('Relative Flux [PPM]')
    plt.show()
    return

# def fit_trapezoid(obj_num, method, pars=[t0, T, tau, depth]):
#     t, f = read_data(obj_num)
#     fun = trapezoid(pars, t)
#     meth = method
#     res = minimize(fun, t, method=meth)
#     return res
