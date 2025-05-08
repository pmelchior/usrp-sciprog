import scipy.optimize as so

def chi2(params, time, flux, stddev):
    model = trapezoid(params, time)
    return np.sum((model - flux)**2 / stddev**2)

def fit_trapezoid(params, time, flux, stddev):
    result = so.minimize(chi2, params, args=(time, flux, stddev))
    return result

stddev = 80
result = fit_trapezoid(params, time, flux, stddev)
plot_fit(time, flux, result.x)
