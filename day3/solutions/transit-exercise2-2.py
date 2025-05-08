t = np.linspace(-1, 1, 100)
params = (100, 1, 0.0, 0.2)

# vary depth
fig = plt.figure()
ax = fig.add_subplot(111)
for delta in [100,200,300,400,500]:
    params_ = list(params)
    params_[0] = delta
    ax.plot(t, trapezoid(params_, t), label=r'$\Delta={}$'.format(delta))
ax.legend(loc='upper right')
    
# vary total length
fig = plt.figure()
ax = fig.add_subplot(111)
for T in [0.5, 1, 1.5, 2]:
    params_ = list(params)
    params_[1] = T
    ax.plot(t, trapezoid(params_, t), label=r'$T={}$'.format(T))
ax.legend(loc='upper right')

# vary mid point
fig = plt.figure()
ax = fig.add_subplot(111)
for t0 in [-0.4, -0.2, 0, 0.2, 0.4]:
    params_ = list(params)
    params_[2] = t0
    ax.plot(t, trapezoid(params_, t), label=r'$t_0={}$'.format(t0))
ax.legend(loc='upper right')

# vary ingress/egress time
fig = plt.figure()
ax = fig.add_subplot(111)
for tau in [0, 0.2, 0.4, 0.6]:
    params_ = list(params)
    params_[3] = tau
    ax.plot(t, trapezoid(params_, t), label=r'$\tau={}$'.format(tau))
ax.legend(loc='upper right')
