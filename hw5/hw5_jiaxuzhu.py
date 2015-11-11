from math import log, exp

def readArrayFile(filename):
    file = open(filename, 'r')
    num = []
    for line in file.readlines():
        line = line.strip(' \n').split(' ')
        if len(line) > 1:
            num.append(map(int, line))
        else:
            num.append(int(line[0]))
    return num

X = readArrayFile('X.txt')
Y = readArrayFile('Y.txt')

def noiseOR(X, Y, p):
    tmp = 1
    for i in range(len(X)):
        tmp *= pow((1 - p[i]), X[i])
    if Y == 1:
        tmp = 1 - tmp
    return tmp

def logLikelihood(X, Y, p):
    tmp = 0.0
    for i in range(len(X)):
        tmp += log(noiseOR(X[i], Y[i], p))
    return tmp / len(X)

def EM(X, Y, p):
    tmp = [0.0] * len(p)
    count = [0] * len(p)
    for i in range(len(X)):
        for j in range(len(p)):
            if X[i][j] == 1:
                count[j] += 1
            tmp[j] += Y[i]*X[i][j]*p[j]/noiseOR(X[i], Y[i], p)
    for i in range(len(p)):
        tmp[i] /= count[i]
    return tmp

def hw5_2():
    p = [0.5]*10
    X = readArrayFile('X.txt')
    Y = readArrayFile('Y.txt')
    index = [0,1,2,4,8,16,32,64]
    for i in range(65):
        if i in index:
            print logLikelihood(X, Y, p)
        p = EM(X, Y, p)

def hw5_3_f(x):
    for i in range(20):
        print x
        x = x - (exp(2*x)-1.0)/(exp(2*x)+1.0)

hw5_3_f(3)