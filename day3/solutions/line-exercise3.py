# create matrices and vectors:

# learn this is a magical function - it makes exactly what we want for this design matrix
X = np.vander(x, N=2, increasing=True)
# OR:
# X = np.vstack((np.ones_like(x), x)).T

Cov = np.diag(y_err**2)
Cinv = np.linalg.inv(Cov) # we need the inverse covariance matrix

# get the parameter covariance matrix ...
pars_Cov = np.linalg.inv(X.T @ Cinv @ X)

# and the best parameters using the new Python matrix operator
best_pars = pars_Cov @ (X.T @ Cinv @ y)
