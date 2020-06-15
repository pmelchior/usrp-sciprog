f, s, xm, ym, w = result.x
theta = 0
model = Gaussian2D.evaluate(X, Y, f, xm, ym, w, w, theta) + s

residual = img - model
plt.imshow(residual)
plt.colorbar()
