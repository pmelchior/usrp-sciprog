data = np.genfromtxt('table1.txt', names=True, dtype=None)

plt.scatter(data['R'], data['V'])
plt.xlabel('R [Mpc]')
plt.ylabel('V [km/s]')
