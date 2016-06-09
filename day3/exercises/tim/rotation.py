import numpy as np


def rotation(angle):
    a = np.deg2rad(angle)
    return np.array([[np.cos(a),np.sin(a)],[-np.sin(a), np.cos(a)]])

if __name__=='__main__':
    print(rotation(30))