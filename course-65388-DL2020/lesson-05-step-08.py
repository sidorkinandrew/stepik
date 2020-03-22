import numpy as np

def no_numpy_scalar(v1, v2):
    #param v1, v2: lists of 3 ints
    #YOUR CODE: please do not use numpy
    result = sum(xi*yi for xi,yi in zip(v1,v2))
    return result

def numpy_scalar (v1, v2):
    #param v1, v2: np.arrays[3]
    result = np.dot(v1,v2)
    return result