#Jiaxu Zhu
#CSE250A hw3.5
from math import log

class TokenEntry:
    totalCount = 0
    def __init__(self, index, unigram, bigram):
        self.index = index
        self.unigram = unigram
        self.bigram = bigram

def pu(token):
    if not token in tokenDict:
        token = '<UNK>'
    return tokenDict[token].unigram / TokenEntry.totalCount

def pb(token1, token2):
    if not token1 in tokenDict:
        token1 = '<UNK>'
    if not token2 in tokenDict:
        token2 = '<UNK>'
    if not token2 in tokenDict[token1].bigram:
        #print 'Not in Corpus %s %s' % (token1, token2)
        return 0
    else:
        return tokenDict[token1].bigram[token2] / tokenDict[token1].unigram

def pm(token1, token2, l):
    return l * pu(token2) + (1-l) * pb(token1, token2)

def lu(sentence):
    tokens = sentence.upper().strip('\n').split(' ')
    p = 1
    for token in tokens:
        p *= pu(token)
    return log(p)

def lb(sentence):
    tokens = sentence.upper().strip('\n').split(' ')
    p = 1
    for i in range(0, len(tokens)):
        if i == 0:
            p *= pb('<s>', tokens[i])
        else:
            p *= pb(tokens[i-1], tokens[i])
    return log(p)

def lm(sentence, l):
    tokens = sentence.upper().strip('\n').split(' ')
    p = 1
    for i in range(0, len(tokens)):
        if i == 0:
            p *= pm('<s>', tokens[i], l)
        else:
            p *= pm(tokens[i-1], tokens[i], l)
    return log(p)


unigram = [];
tokenList =[]
tokenDict = {}
tokenFile = open('vocab.txt', 'r')
index = 0
for token in tokenFile.readlines():
    token = token.strip('\n');
    tokenList.append(token)
    tokenDict[token] = TokenEntry(index, 0, {})

unigramFile = open('unigram.txt', 'r')
for line in unigramFile.readlines():
    tokenDict[tokenList[index]].unigram = float(line)
    TokenEntry.totalCount += tokenDict[tokenList[index]].unigram
    index += 1

bigramFile = open('bigram.txt', 'r')
for line in bigramFile.readlines():
    line = line.split('\t');
    index1 = int(line[0]) - 1
    index2 = int(line[1]) - 1
    count = float(line[2])
    tokenDict[tokenList[index1]].bigram[tokenList[index2]] = count

for token in tokenList:
    if token[0] == 'M':
        print '%s & %f \\\\' % (token, tokenDict[token].pu())
        print '\\hline'

b = sorted(tokenDict['THE'].bigram.items(), key=lambda x: x[1], reverse=True)
for iter in range(0, 10):
    print '%s & %f \\\\' % (b[iter][0], b[iter][1] / tokenDict['THE'].unigram)
    print '\\hline'

print lu('The stock market fell by one hundred points last week')
print lb('The stock market fell by one hundred points last week')

print lu('The sixteen officials sold fire insurance')
print lb('The sixteen officials sold fire insurance')

for l in range(1,101):
    print lm('The sixteen officials sold fire insurance', float(l)/100)