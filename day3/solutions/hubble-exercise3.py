X = np.column_stack((data['R'], np.cos(ra_)*np.cos(dec_), np.sin(ra_)*np.cos(dec_), np.sin(dec_)))

theta_s = np.linalg.inv(X.T @ X) @ X.T @ data['V']
v_s = X[:,1:] @ theta_s[1:]
plt.scatter(data['R'], data['V']- v_s)
plt.xlabel('R [Mpc]')
plt.ylabel('V - Vs[km/s]')

r_ = np.linspace(0,2,100)
v_ = theta_s[0] * r_
plt.plot(r_, v_, c='r')
