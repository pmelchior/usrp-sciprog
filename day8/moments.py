import numpy

def makeCoordinateArrays(shape):
    x1d = numpy.arange(shape[1])
    y1d = numpy.arange(shape[0])
    return numpy.meshgrid(x1d, y1d)

def computeMoments(image, mask, x, y):
    masked_image = image[mask]
    masked_x = x[mask]
    masked_y = y[mask]
    m0 = masked_image.sum()
    mx = (masked_x * masked_image).sum()/m0
    my = (masked_y * masked_image).sum()/m0
    mxx = (masked_x**2 * masked_image).sum()/m0
    myy = (masked_y**2 * masked_image).sum()/m0
    mxy = (masked_x * masked_y * masked_image).sum()/m0
    return m0, mx, my, mxx, myy, mxy

def drawGaussian(mx, my, mxx, myy, mxy, x, y):
    C = numpy.array([[mxx, mxy], [mxy, myy]], dtype=float)
    zx = x - mx
    zy = y - my
    C_inv = numpy.linalg.inv(C)   # or C.I if C is a numpy.matrix
    s = C_inv[0,0]*zx**2 + C_inv[1,1]*zy**2 + 2*(C_inv[0,1]*zx*zy)
    result = numpy.exp(-0.5*s)
    result /= result.sum()   # or result = result / result.sum()
    return result
    