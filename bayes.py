# import re
#
# mySent = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'
# # 按空格切分
# # print(mySent.split())
# regEx = re.compile('\\W')
# listOfTokens = regEx.split(mySent)
#
# print("正则表达式切分：", listOfTokens)
# lst = [tok.lower() for tok in listOfTokens if len(tok) > 0]
# print(lst)
from numpy import *

"""文本构建词向量"""


#
# def loadDataSet():
#     postingList = [
#         ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
#         ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
#         ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
#         ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
#         ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
#         ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
#     ]
#     classVec = [0, 1, 0, 1, 0, 1]
#     return postingList, classVec
def load_data(filename):
    data = []
    label = [0, 1, 0, 1, 0, 1]
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.split()
        data.append(lineArr)
    return data, label


"""创建一个包含所有文档的词典列表"""""


def createVocalList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        # 创建两个集合的并集
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in inputSet:
            returnVec[vocabList.index(word)] += 1
        else:
            print("the word:{}s not in my Vocabulary!".format(word))
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0 = 1 - pAbusive
    p0Num = zeros(numWords)
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num / p1Denom  # p(w|c1)
    p0Vect = p0Num / p0Denom  # p(w|c2)
    return p0, pAbusive, p0Vect, p1Vect


def classifyNB(vec2Classify, p0, p1, p0V, p1V):
    p1_class = sum(vec2Classify * p1 * p1V)
    p0_class = sum(vec2Classify * p0 * p0V)
    if p1_class > p0_class:
        return 1
    else:
        return 0


if __name__ == "__main__":
    listOposts, listClasses = load_data('text.txt')
    myVocabList = createVocalList(listOposts)
    trainMat = []
    for postinDoc in listOposts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0, pAbusive, p0V, p1V = trainNB0(array(trainMat), array(listClasses))
    testSentence = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testSentence))
    print(testSentence,"classified as:",classifyNB(thisDoc, p0, pAbusive, p0V, p1V))
    testSentence = ['stupid','garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testSentence))
    print(testSentence,"classified as:",classifyNB(thisDoc, p0, pAbusive, p0V, p1V))
    # pass