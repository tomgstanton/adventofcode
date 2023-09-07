import re
import itertools

dir = '2015/Day 13/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Scores():
    def __init__(self,):
        self.people = []
        self.happiness = []
        self.bestscore = 0
        self.bestorder = []

def ExtractNumber(x):
    string = x.replace('lose ','-')
    extracted = re.findall(r'[-+]?\d+',str(string))
    return [int(s) for s in extracted]

def ExtractDetails(line):
    change = ExtractNumber(line)
    splits = line.split()
    if splits[0] not in scores.people:
        scores.people.append(splits[0])
    scores.happiness.append([[splits[0],splits[-1][0:-1]],change[0]])

def Score(pair):
    for x in scores.happiness:
        if pair == x[0]:
            return x[1]

def ScoreHappinessChange(order):
    output = 0
    for index in range(len(order)):
        if index == 0: 
            pair = [order[-1],order[0]]
            reverse_pair = [order[0],order[-1]]
        else:            
            pair = [order[index-1],order[index]]
            reverse_pair = [order[index],order[index-1]]
        output += Score(pair)
        output += Score(reverse_pair)
    if output > scores.bestscore:
        scores.bestscore = output
        scores.bestorder = order

def Calculate(lines):
    for line in lines:
        ExtractDetails(line)
    permutations = itertools.permutations(scores.people)
    for x in permutations:
        ScoreHappinessChange(x)
    return scores.bestscore
    
scores = Scores()
answer = Calculate(inputlines)
print('Answer is:',answer)