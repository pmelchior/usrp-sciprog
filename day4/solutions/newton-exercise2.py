x0 = (0,0)
p = 2
result = so.minimize(h, x0, args=(p,))

x_ = np.linspace(-10,10,100)
xy = np.dstack(np.meshgrid(x_,x_))
plt.imshow(h(xy, p), extent=(-10,10,-10,10), cmap='viridis')
plt.scatter(*result.x, c='r',zorder=10)
