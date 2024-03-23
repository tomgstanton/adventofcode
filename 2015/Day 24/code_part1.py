import itertools
import math

dir = '2015/Day 24/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def GetWeights(inputlines):
    output = []
    for line in inputlines:
        if line[-1] == '\n':
            line = line[:-1]
        output.append(int(line))
    return output

def GetGroupings(listofweights,thirdweight):
    output = []
    print(len(listofweights))
    stop = False
    while stop == False:
        for number in range(len(listofweights)):
            if len(output) != 0:
                break
            combinations = itertools.combinations(listofweights,number)
            for combo in combinations:
                batchweight = sum(combo)
                if batchweight > thirdweight:
                    stop = True
                if batchweight == thirdweight:
                    output.append(combo)
                if batchweight < thirdweight:
                    stop == False
    return output

def Calculate(inputlines):
    answer = 999999999999
    weights = GetWeights(inputlines)
    thirdweight = sum(weights) / 3
    batches = GetGroupings(weights,thirdweight)
    for batch in batches:
        quantumentanglement = math.prod(batch)
        if quantumentanglement < answer:
            answer = quantumentanglement
    return answer

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)