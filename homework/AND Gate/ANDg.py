import gd2 as g
import math as m
import numpy as np

def sig(t):
    return 1.0/(1.0+m.exp(-t))

A = np.array([[0.0, 0, 0],
                [0, 1, 0],
                [1, 0, 0],
                [1, 1, 1]])
B = np.array([[0.0, 0, 0, 1]]).transpose()

def f(p):
    X = p
    Y = A.dot(X)    #AX
    return norm(Y-B)

p = np.array([0.0, 0 ,0])
g.gradientDescendent(f, p)