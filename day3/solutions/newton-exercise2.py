x0 = (0,0)
p = 2
result = so.minimize(h, x0, args=(p,))

# generate x, y points
x_ = np.linspace(-10,10,100)
y_ = np.linspace(-10,10,100)
# expand each coordinate into 2D grid
xx_, yy_ = np.meshgrid(x_,x_)
# stack them to make a Nx*Ny*2 array
xy = np.dstack([xx_,yy_])
plt.pcolormesh(x_,x_,h(xy, p))
plt.gca().set_aspect("equal")
plt.scatter(*result.x, c='r',zorder=10)
