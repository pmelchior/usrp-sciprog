import numpy as np


def rotation(angle):
    a = np.deg2rad(angle)
    return np.array([[np.cos(a),np.sin(a)],[-np.sin(a), np.cos(a)]])

def circle(npoints=18):
    """Returns (x,y) coordinates for npoints around circle
    """
    angles = np.deg2rad(np.linspace(0,360,npoints,False))
    return np.array([[np.cos(a), np.sin(a)] for a in angles])

if __name__=='__main__':
    print(rotation(30))