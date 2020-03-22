import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param first: list of "size" lists, each contains "size" floats
    """
    result = []
    #YOUR CODE: please do not use numpy
    result = [[sum(a*b for a,b in zip(first_row,second_col)) for second_col in zip(*second)] for first_row in first]
    return result

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """

    #YOUR CODE: please use numpy

    result = np.matmul(first, second)
    return result