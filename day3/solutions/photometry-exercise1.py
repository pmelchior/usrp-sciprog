%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

hdu = fits.open("data/point-source.fits")
img = hdu[0].data
plt.imshow(img, origin="lower")
plt.colorbar()
