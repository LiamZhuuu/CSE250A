__author__ = 'jiaxuzhu'

from utils import *
from math import *
import matplotlib.pyplot as plt
import scipy.io as sio
def digitGradient(x0, x1, w, eta):
    g = [0] * len(w)
    for i in range(len(x0)):
        delta = 0 - sigmod(dot(x0[i], w))
        for j in range(len(w)):
            g[j] += delta * x0[i][j]
    for i in range(len(x1)):
        delta = 1 - sigmod(dot(x1[i], w))
        for j in range(len(w)):
            g[j] += delta * x1[i][j]
    for i in range(len(w)):
        w[i] += eta * g[i]
    return w

def digitErrorRate(x0, x1, w0, w1):
    count = 0
    for i in range(len(x0)):
        if sigmod(dot(x0[i], w0)) > sigmod(dot(x0[i], w1)):
            count += 1
    for i in range(len(x1)):
        if sigmod(dot(x1[i], w1)) > sigmod(dot(x1[i], w0)):
            count += 1
    return float(count) / (len(x0)+len(x1))

def digitLikelihood(x0, x1, w):
    l = 0
    for i in range(len(x0)):
        l += log(sigmod(-dot(x0[i],w)))
    for i in range(len(x1)):
        l += log(sigmod(dot(x1[i], w)))
    return l

def digitClassification():
    train3 = readArrayFile('new_train3.txt')
    train5 = readArrayFile('new_train5.txt')
    test3 = readArrayFile('new_test3.txt')
    test5 = readArrayFile('new_test5.txt')
    w3 = [0] * 64
    w5 = [0] * 64
    l3 = []
    l5 = []
    for i in range(2500):
        w3 = digitGradient(train5, train3, w3, 1e-4)
        w5 = digitGradient(train3, train5, w5, 1e-4)
        l3.append(digitLikelihood(train5, train3, w3))
        l5.append(digitLikelihood(train3, train5, w5))
    sio.savemat('hw4.6.mat',{'l3':l3,'l5':l5,'w3':w3,'w5':w5})
    print digitErrorRate(train3, train5, w3, w5)
    print digitErrorRate(test3, test5, w3, w5)

