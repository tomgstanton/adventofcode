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

def GetGroupings(listofweights,fourthweight):
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
                if batchweight > fourthweight:
                    stop = True
                if batchweight == fourthweight:
                    output.append(combo)
                if batchweight < fourthweight:
                    stop == False
    return output

def Calculate(inputlines):
    answer = 999999999999
    weights = GetWeights(inputlines)
    fourthweight = sum(weights) / 4
    batches = GetGroupings(weights,fourthweight)
    for batch in batches:
        quantumentanglement = math.prod(batch)
        if quantumentanglement < answer:
            answer = quantumentanglement
    return answer

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)