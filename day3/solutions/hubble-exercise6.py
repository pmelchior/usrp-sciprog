Sigma_1 = 1/scatter.var() * np.eye(N)
Sigma_Cov = np.linalg.inv(X.T @ Sigma_1 @ X)
theta_err = Sigma_Cov @ X.T @ Sigma_1 @ data['V']

H0 = theta_err[0]
dH0 = np.sqrt(Sigma_Cov[0,0])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data['R'], data['V'] - v_s)
ax.plot(r_, H0*r_, 'k-')
ax.plot(r_, (H0-dH0)*r_, 'k--')
ax.plot(r_, (H0+dH0)*r_, 'k--')
ax.set_xlabel('Distance [Mpc]')
ax.set_ylabel('Velocity [km/s]')
