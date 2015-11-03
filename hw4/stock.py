__author__ = 'jiaxuzhu'

from utils import *
from math import *

def stockGradient(x, w, eta):
    g = [0] * len(w)
    for i in range(len(w), len(x)):
        delta = x[i] - dot(w, x[i-len(w):i])
        for j in range(0, len(w)):
            g[j] += delta * x[i-len(w)+j]
    for i in range(len(w)):
        w[i] += eta * g[i]
    return w

def stockP(x, w):
    tmp = x[-1]
    for i in range(len(w)):
        tmp -= w[i] * x[i]
    tmp = -0.5 * log(2*pi) - 0.5 * pow(tmp, 2)
    return tmp

def stockError(x, w):
    p = 0.0
    for i in range(len(w), len(x)):
        p += pow(x[i] - dot(w, x[i-len(w):i]), 2)
    return p / (len(x) - len(w))

def stockLearning():
    trainData = readArrayFile('nasdaq00.txt')
    testData = readArrayFile('nasdaq01.txt')
    w = [0, 0, 0]
    for i in range(20000):
        print stockError(trainData, w)
        w = stockGradient(trainData, w, 1e-10)
        #print w
    print w
    print stockError(trainData, w)
    print stockError(testData, w)