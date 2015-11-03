#Jiaxu Zhu
#CSE250A hw3.2
from random import randint
from math import pow

#from decimal to binary
def decimal(B):
    f = 0
    base = 1
    for i in range(0, len(B)):
        f += base * B[i]
        base *= 2
    return f

randomB = lambda length: [randint(0,1) for b in range(0, length)]
n = 10
alpha = 0.35
numerator = 0
denominator = 0
Z = 64
p = 0
for iter in range(0, 1000000):
    B = randomB(n)
    f = decimal(B)
    pEx = (1-alpha)/(1+alpha) * pow(alpha, abs(Z - f))
    denominator += pEx
    if B[6] == 1:
        numerator += pEx
    if denominator > 0:
        p = numerator / denominator
    if (iter+1) % 20000 == 0:
        print p

