def plot_fit(time, flux, params):
    
    fig = plt.figure(figsize=(6,8))
    ax1 = fig.add_subplot(211)
    ax1.scatter(time, flux)
    
    t = np.linspace(-1, 1, 100)
    model = trapezoid(params, t)
    ax1.plot(t, model, color='C3')
    ax1.set_ylabel('relative flux')
    
    ax2 = fig.add_subplot(212, sharex=ax1)
    
    model_at_time = trapezoid(params, time)
    ax2.scatter(time, flux - model_at_time)
    ax2.axhline(0, color='C3')
    ax2.set_xlabel('time')
    ax2.set_ylabel('data - model')
    return ax
    
plot_fit(time, flux, params)
