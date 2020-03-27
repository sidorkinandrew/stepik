from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import torch

A = [[1, -47, 25, -3], [10, 17, -15, 22], [-3, -7, 26, 36], [12, -27, -42, 0]]
B = [[-50, -13, 1, 10, 1242], [21, 48, -13, -14, -20], [20, 15, 11, 43, 11], [11, 103, 147, 27, -8]]
A = torch.tensor(A, dtype = torch.float)
B = torch.tensor(B, dtype = torch.float)
def get_cos_sim(A, B):
    """
        A, B - torch float tensors
        A, B needs normalizing
    """
    return torch.mean(torch.matmul(A/torch.norm(A, dim=1, keepdim=True),(B/torch.norm(B, dim=0, keepdim=True))))

get_cos_sim(A, B)