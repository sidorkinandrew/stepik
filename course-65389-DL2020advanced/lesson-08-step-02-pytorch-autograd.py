from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import torch

def find_x_derivative(x, y):
    x = torch.tensor([x], dtype=float, requires_grad=True)
    y = torch.tensor([y], dtype=float)
    z = torch.sin(torch.tan(x)*(x*x/y) + torch.log( torch.exp(-x*x+3) + x*x*x*y) ) * torch.tan( x*x*(torch.exp(x**9)))
    z.backward()
    return x.grad

find_x_derivative(1, 21)