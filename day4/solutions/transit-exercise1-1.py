import numpy as np

num = 7016.01

def read_data(num):
    filename = 'data/{}.txt'.format(num)
    data = np.loadtxt(filename)
    time = data[:,0]
    flux = data[:,1]
    return time, flux

time, flux = read_data(num)
