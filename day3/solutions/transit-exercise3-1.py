t = np.linspace(-1, 1, 100)
params = (200, 0.7, 0.0, 0.2)
model = trapezoid(params, t)

ax = plot_data(time, flux)
ax.plot(t, model, color='C3')
