from astropy.modeling.functional_models import Gaussian2D
Ny, Nx = img.shape
X, Y = np.meshgrid(np.arange(Nx), np.arange(Ny))

model = Gaussian2D.evaluate(X, Y, 1, 16, 16, 3, 3, 0)
plt.imshow(model, origin="lower")
