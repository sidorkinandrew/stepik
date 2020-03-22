import numpy as np
def diag_2k(a):
    #param a: np.array[size, size]
    result = sum(i for i in a.diagonal() if not i%2)
    return result