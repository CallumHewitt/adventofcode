import functools
import math

input1FileName = 'input1.txt'
input2FileName = 'input2.txt'

def getInput(inputNum):
    fileName = getInputFileName(inputNum)
    print('Getting input as string from ' + fileName)
    return open(getInputFileName(inputNum), 'r').read()

def getInputFileName(inputNum):
    return input1FileName if inputNum == 1 else input2FileName

def getInputAsList(inputNum):
    fileName = getInputFileName(inputNum)
    print('Getting input as list from ' + fileName)
    return open(getInputFileName(inputNum), 'r').readlines()

def mapAndSum(mapFunc, iterable, debug=False):
    result = -1
    mappedData = list(map(mapFunc, iterable))
    if (debug):
        print('Mapped data: ' + str(mappedData))
    return functools.reduce(lambda a,b: a + b, mappedData)