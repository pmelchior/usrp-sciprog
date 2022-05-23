from astropy.modeling.functional_models import Gaussian2D
X, Y = np.meshgrid(np.arange(33), np.arange(33))

model = Gaussian2D.evaluate(X, Y, 1, 16, 16, 3, 3, 0)
plt.imshow(model)
