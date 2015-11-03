# CSE250A HW1
# Jiaxu Zhu
import string

# Function to derive beat guess and its probability
def bestGuess(wordNum, words, wordCount, correctGuess, wrongGuess):
    tag = []
    guess = [0] * 26
    guessChar = string.uppercase
    sumCount = 0
    # find words whose P(W|E) > 0
    for i in range(wordNum):
        word = words[i]
        check = True
        for j in range(5):
            if (correctGuess[j] == '*' and word[j] in correctGuess) or \
                    (correctGuess[j] != '*' and correctGuess[j] != word[j]):
                check = False
                break
            if word[j] in wrongGuess:
                check = False
                break
        if not check:
            tag.append(0)
        else:
            tag.append(1)
            sumCount += wordCount[i]
    # sum P(L|W)
    for i in range(wordNum):
        if tag[i] == 0:
            continue
        p = float(wordCount[i]) / sumCount
        for l in range(26):
            if not guessChar[l] in correctGuess and not guessChar[l] in wrongGuess and guessChar[l] in words[i]:
                guess[l] += p
    # get best guess with max probability
    maxP = max(guess)
    best = chr(65+guess.index(maxP))
    return [best, maxP]
# pre process
inputFile = open('hw1_word_counts_05.txt')
words = []
wordCount = []

for line in inputFile.readlines():
    data = line.strip('\n').split(' ')
    words.append(data[0])
    wordCount.append(int(data[1]))
# sort words according to count number
wordNum = len(words)
sortIndex = sorted(range(wordNum), key=lambda k: wordCount[k], reverse=True)

for i in range(0, 8):
    index = sortIndex[i]
    print words[index], wordCount[index]

for i in range(wordNum - 8, wordNum):
    index = sortIndex[i]
    print words[index], wordCount[index]

# compute 1.7 b)
print bestGuess(wordNum, words, wordCount, '*****', [])
print bestGuess(wordNum, words, wordCount, '*****', ['E', 'O'])
print bestGuess(wordNum, words, wordCount, 'D**I*', [])
print bestGuess(wordNum, words, wordCount, 'D**I*', ['A'])
print bestGuess(wordNum, words, wordCount, '*U***', ['A', 'I', 'E', 'O', 'S'])
