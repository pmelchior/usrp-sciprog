import scipy.optimize as so

def chi2(params, img, X, Y):
    f, s, xm, ym, w = params
    theta = 0
    model = Gaussian2D.evaluate(X, Y, f, xm, ym, w, w, theta) + s
    return np.sum((img - model)**2 / img)

x0 = (168.521, 98.409, 16., 16., 3.)

result = so.minimize(chi2, x0, args=(img, X, Y,))
print(result)
