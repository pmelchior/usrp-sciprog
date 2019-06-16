N = len(data)
X = data['R'].reshape(N,1)
theta = np.linalg.inv(X.T @ X) @ X.T @ data['V']

plt.scatter(data['R'], data['V'])
plt.xlabel('R [Mpc]')
plt.ylabel('V [km/s]')

r_ = np.linspace(0,2,100)
v_ = theta[0] * r_
plt.plot(r_, v_, c='r')
