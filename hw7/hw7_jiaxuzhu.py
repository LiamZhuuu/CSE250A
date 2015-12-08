gamma = 0.99
sNum = 81
import numpy as np

def readArrayFile(filename):
    file = open(filename, 'r')
    num = []
    for line in file.readlines():
        line = line.strip(' \n').split('  ')
        if len(line) == 1:
            line = line[0].split(' ')
        if len(line) > 1:
            num.append(map(float, line))
        else:
            num.append(float(line[0]))
    return num


def getTransP():
    trans = []
    for i in range(1,5):
        filename = 'prob_a%d.txt' % (i)
        p_a = readArrayFile(filename)
        tmp = [[0 for x in range(sNum)] for x in range(sNum)]
        for i in range(len(p_a)):
            tmp[int(p_a[i][0])-1][int(p_a[i][1])-1] = p_a[i][2]
        trans.append(tmp)
    return trans

def mazePrint(v, width):
    tmp = [[0 for x in range(width)] for x in range(width)]
    x = 0
    y = 0
    for i in range(len(v)):
        tmp[x][y] = v[i]
        x += 1
        if x == width:
            x = 0
            y += 1
    for i in range(width):
        for j in range(width):
            if j != width-1:
                print '%.2f & ' % (tmp[i][j]),
            else:
                print '%.2f \\\\ ' % (tmp[i][j])
        print '\\hline'
    print

def policyPrint(v, width):
    tmp = [[0 for x in range(width)] for x in range(width)]
    x = 0
    y = 0
    policy = ['WEST', 'NORTH', 'EAST', 'SOUTH']
    for i in range(len(v)):
        tmp[x][y] = v[i]
        x += 1
        if x == width:
            x = 0
            y += 1
    for i in range(width):
        for j in range(width):
            if tmp[i][j] != -1:
                print policy[tmp[i][j]],
            else:
                print '*',
            if j != width -1:
                print ' &',
            else:
                print '\\\\'
        print '\\hline'
    print

def valueIteration():

    reward = readArrayFile('rewards.txt')
    trans = getTransP()
    vk = [0.0] * sNum
    vk1 = [0.0] * sNum
    pi = [-1] * sNum
    for iter in range(2000):
        for i in range(sNum):
            maxValue = float("-inf")
            for a in range(4):
                tmp = 0
                for j in range(sNum):
                    tmp += trans[a][i][j] * vk[j]
                if tmp > maxValue:
                    maxValue = tmp
                    if tmp > 0:
                        pi[i] = a
            vk1[i] = reward[i] + gamma * maxValue
        for i in range(sNum):
            vk[i] = vk1[i]
    mazePrint(vk1, 9)
    policyPrint(pi, 9)

def policyIteration():
    reward = readArrayFile('rewards.txt')
    trans = getTransP()
    v = [0.0] * sNum
    pi = [0] * sNum
    for iter in range(20):
        p = np.zeros((sNum, sNum))
        for i in range(sNum):
            for j in range(sNum):
                p[i,j] = trans[pi[i]][i][j]
        p = p *gamma
        v = np.linalg.inv(np.identity(sNum,  dtype=float) - p) * np.matrix(reward).transpose()
        for i in range(sNum):
            maxValue = float("-inf")
            for a in range(4):
                tmp = 0
                for j in range(sNum):
                    tmp += trans[a][i][j] * v[j]
                if tmp > maxValue:
                    maxValue = tmp
                    if tmp > 0:
                        pi[i] = a
    policyPrint(pi, 9)

#trans = getTransP()
#valueIteration()
policyIteration()