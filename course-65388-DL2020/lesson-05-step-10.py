import numpy as np

def cumsum(A):
    #param A: np.array[m,n]
    #YOUR CODE

    result = np.cumsum(A, axis=-1) 
    return result