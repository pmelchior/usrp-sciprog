data = np.genfromtxt('table1.txt', names=True, dtype=None, encoding='utf8')

plt.scatter(data['R'], data['V'])
plt.xlabel('R [Mpc]')
plt.ylabel('V [km/s]')
