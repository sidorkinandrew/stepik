import numpy as np

def transform(X, a=1):
    """
    param X: np.array[batch_size, n]
    """
    result = []
    for arow in X:
        _ = np.array(arow)
        _[::-2] = arow[::2]**3
        _[1::2] = a
        result.append(np.append(arow,_))
    return result