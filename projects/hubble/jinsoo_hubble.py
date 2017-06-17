import numpy as np
import matplotlib.pyplot as plt
import coordinates as coord

data = np.genfromtxt("table1.txt",dtype=None,names=True)
print(data)
N = len(data)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(data['R'],data['V'])
# ax.set_xlim(0.0,2.5)
# ax.set_xlabel('Distance [Mpc]')
# ax.set_ylabel('Radial Velocity [km/s]')
# plt.show()

# solving for 1 parameter H0
X1 = data['R'].reshape(N,1) #design matrix
params, _, _, _ = np.linalg.lstsq(X1, data['V'])
H0 = params[0]

R = np.linspace(0,2.5,100)
# ax.plot(R, H0*R, 'k--')
# plt.show()

# solving for 2 parameters H0 and c
X2 = np.empty([N,2])
X2[:,0] = data['R']
X2[:,1] = 1.0
params_c, _, _, _ = np.linalg.lstsq(X2, data['V'])
H0_c = params_c[0]
c = params_c[1]

# ax.plot(R, H0_c*R + c, 'b--')
# plt.show()

# solving for 4 parameters H0, X, Y, Z - generalized
Xg = np.empty([N,4])
ra_deg = coord.Ra2Deg(data['RA'])
dec_deg = coord.Dec2Deg(data['DEC'])
Xg[:,0] = data['R']
Xg[:,1] = np.cos(ra_deg*np.pi/180)*np.cos(dec_deg*np.pi/180)
Xg[:,2] = np.sin(ra_deg*np.pi/180)*np.cos(dec_deg*np.pi/180)
Xg[:,3] = np.sin(dec_deg*np.pi/180)

params_g, _, _, _ = np.linalg.lstsq(Xg, data['V'])
H0_g = params_g[0]
X = params_g[1]
Y = params_g[2]
Z = params_g[3]

VS = X*Xg[:,1] + Y*Xg[:,2] + Z*Xg[:,3]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data['R'],data['V']-VS)
ax.set_xlim(0.0,2.5)
ax.set_xlabel('Distance [Mpc]')
ax.set_ylabel('Radial Velocity [km/s]')
ax.plot(R, H0_g*R,'k--')

#age of universe using H0_g
Mpc = 3.08e19 #in km
t = (H0_g * (1/Mpc))**(-1)
bln = 3.154e16 #bln yr in seconds
t = t/bln
print(t)
