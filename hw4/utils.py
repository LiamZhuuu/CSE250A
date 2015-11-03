__author__ = 'jiaxuzhu'

from math import exp
def dot(x,y):
    tmp = [x[i]*y[i] for i in range(len(x))]
    return sum(tmp)

def sigmod(z):
    return 1.0 / (1.0 + exp(-z))

def readArrayFile(filename):
    file = open(filename, 'r')
    num = []
    for line in file.readlines():
        line = line.strip(' \n').split(' ')
        if len(line) > 1:
            num.append(map(float, line))
        else:
            num.append(float(line[0]))
    return num

