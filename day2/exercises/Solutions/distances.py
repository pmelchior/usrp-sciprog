import numpy as np
from scipy.spatial.distance import cdist


def double_loop(coord1, coord2):
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
    #Declare an array full of zeros to store the results
    result = np.zeros((np.int(coord1.shape[0]), np.int(coord2.shape[0])))
    #for each coordinate in coord1
    for i in range(coord1.shape[0]):
        #for each coordinate in coord2
        for j in range(coord2.shape[0]):
            tmp = 0
            #for each component of each coordinate
            for k in range(coord1.shape[1]):
                #compute the square of the difference between the two coordinates
                tmp += (coord1[i, k] - coord2[j, k]) ** 2
            #store the sum over the components in an array
            result[i, j] = tmp
    #returns the square root of the array, i.e the eusclidean distance between each point of each set
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
    #Declare an array to store the results
    result = np.zeros((np.int(coord1.shape[0]), np.int(coord2.shape[0])))
    #For each coordinate in coord1
    for i,c in enumerate(coord1):
        #compute the square of the Euclidean distance to all coordinates in the other dataset
        result[i,:] = ((c[0]-coord2[:,0])**2+(c[1]-coord2[:,1])**2)
    #returns the euclidean distance between each point of each dataset
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
    #Same as previously, but coordinates are inverted
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
    #Number of points in each dataset
    n1,n2 = np.int(coord1.shape[0]), np.int(coord2.shape[0])
    #coordinates of the correspondanc points the two datasets (not obvious, please ask me)
    rows, cols = np.where(np.zeros((n1,n2))==0)
    
    #reshaping to match the expected output format
    rows = rows.reshape(n1,n2)
    cols = cols.reshape(n1,n2)
    #compute distance by associating results to the positionsof each coordinate in its own dataset (again, not necessarily easy to follow)
    distances = np.sqrt(np.sum((coord1[rows, :] - coord2[cols, :]) ** 2, axis=2))
    #return the distances
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
    #Scipy actually knows how to do this, so why not try it
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
    #The magic of newaxis broadcasting!
    return np.sqrt(np.sum((coord1[:, np.newaxis, :] - coord2[np.newaxis, :, :]) ** 2, axis=2))
