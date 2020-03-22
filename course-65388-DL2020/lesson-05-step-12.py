import numpy as np
from itertools import groupby

def encode(a):
    result = zip(*((key, len(tuple(group))) for key, group in groupby(a)))
    return tuple(map(np.array,result))