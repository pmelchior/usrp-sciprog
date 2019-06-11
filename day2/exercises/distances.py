import numpy as np
from scipy.spatial.distance import cdist


def naive(coord1, coord2):
    '''Returns the distance between points in two sets of coordinates.
	This function uses loops over all elements in each dataset to get the distances.
	That is the most naive implementation of this function.

    Parameters
    coord1: array
    	coordinates of the first dataset
    coord2: array
    	coordinates of the second dataset

    Returns
	distances: array
		array of the distances between all points in coord1 and all points in coord2

	'''
    result = np.zeros((np.int(coord1.shape[0]), np.int(coord2.shape[0])))
    for i in range(coord1.shape[0]):
        for j in range(coord2.shape[0]):
            tmp = 0
            for k in range(coord1.shape[1]):
                tmp += (coord1[i, k] - coord2[j, k]) ** 2
            result[i, j] = tmp
    return np.sqrt(result)


def one_loop(coord1, coord2):
    '''Returns the distance between points in two sets of coordinates.
    This function uses loops over all elements in each dataset to get the distances.
    Here we don't loop over the dimensions of the coordinate systems.

    Parameters
    coord1: array
        coordinates of the first dataset
    coord2: array
        coordinates of the second dataset

    Returns
    distances: array
        array of the distances between all points in coord1 and all points in coord2

    '''
    result = np.zeros((np.int(coord1.shape[0]), np.int(coord2.shape[0])))

    for i,c in enumerate(coord1):
        result[i,:] = ((c[0]-coord2[:,0])**2+(c[1]-coord2[:,1])**2)
    return np.sqrt(result)


def one_loop_reverse(coord1, coord2):
    '''Returns the distance between points in two sets of coordinates.
    This function uses loops over all elements in each dataset to get the distances.
    Here we don't loop over the dimensions of the coordinate systems.

    Parameters
    coord1: array
        coordinates of the first dataset
    coord2: array
        coordinates of the second dataset

    Returns
    distances: array
        array of the distances between all points in coord1 and all points in coord2

    '''
    result = np.zeros((np.int(coord1.shape[0]), np.int(coord2.shape[0])))

    for i,c in enumerate(coord2):
        result[:,i] = ((c[0]-coord1[:,0])**2+(c[1]-coord1[:,1])**2)
    return np.sqrt(result)


def with_indices(coord1, coord2):
    '''Returns the distance between points in two sets of coordinates.

    This function uses manipulations on indices to compute the distances between all points in both datasets

       Parameters
       coord1: array
           coordinates of the first dataset
       coord2: array
           coordinates of the second dataset

       Returns
    distances: array
        array of the distances between all points in coord1 and all points in coord2

    '''
    n1,n2 = np.int(coord1.shape[0]), np.int(coord2.shape[0])
    rows, cols = np.where(np.zeros((n1,n2))==0)
    rows = rows.reshape(n1,n2)#np.indices((coord1.shape[0], coord2.shape[0]))
    cols = cols.reshape(n1,n2)
    distances = np.sqrt(np.sum((coord1[rows, :] - coord2[cols, :]) ** 2, axis=2))
    return distances


def scipy_version(coord1, coord2):
    '''Returns the distance between points in two sets of coordinates.

    This function uses a function in the scipy library to compute the distances between all points in both datasets

       Parameters
       coord1: array
           coordinates of the first dataset
       coord2: array
           coordinates of the second dataset

       Returns
    distances: array
        array of the distances between all points in coord1 and all points in coord2

    '''
    return cdist(coord1, coord2)


def newaxis_magic(coord1, coord2):
    '''Returns the distance between points in two sets of coordinates.

    This function uses tensor broadcasting to compute the distances between all points in both datasets

       Parameters
       coord1: array
           coordinates of the first dataset
       coord2: array
           coordinates of the second dataset

       Returns
    distances: array
        array of the distances between all points in coord1 and all points in coord2

    '''
    return np.sqrt(np.sum((coord1[:, np.newaxis, :] - coord2[np.newaxis, :, :]) ** 2, axis=2))
