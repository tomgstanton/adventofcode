import itertools
import math

dir = '2015/Day 15/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Ingredients():
    def __init__(self,):
        self.ingredients = []
        self.ratios = Function(100,4)

def MakeDictionary(inputlines):
    dict = {}
    for line in inputlines:
        line = line.replace('\n','')
        line = line.replace(',','')
        elements = line.split(' ')
        ingredient = elements[0][:-1]
        cookie.ingredients.append(ingredient)
        new_dict = {}
        new_elements = elements[1:]
        for item in new_elements:
            if new_elements.index(item)%2 == 0:
                new_dict[item] = int(new_elements[new_elements.index(item)+1])
        dict[ingredient] = new_dict
    return dict

grand_total = 100

def GetNumbers(quantity,maximum,number):
    output = []
    count = min(quantity,maximum)
    for x in range(quantity+1):
        output.append(count)
        if count == math.ceil(quantity/number):
            break
        count -= 1
    return output

def Function(quantity,number):
    output = []
    temp0 = GetNumbers(quantity,100,number)
    for x in temp0:
        new_quant = grand_total-x
        temp1 = GetNumbers(new_quant,x,number-1)
        for y in temp1:
            new_quant = grand_total-x-y
            temp2 = GetNumbers(new_quant,y,number-2)
            for z in temp2:
                new_quant = grand_total-x-y-z
                temp3 = GetNumbers(new_quant,z,number-3)
                for a in temp3:
                    output.append([x,y,z,a])
    return output

def IngredientScore(number,dict):
    output = []
    for x in dict:
        value = dict[x]*number
        output.append(value)
    return output

def ScoreRatio(combo,ingredients,dict):
    scores = []
    for x in range(len(combo)):
        score = IngredientScore(combo[x],dict[ingredients[x]])
        scores.append(score)
    rejigged_scores = [list(i) for i in zip(*scores)]
    calories_scores = rejigged_scores[-1]
    rejigged_scores = rejigged_scores[0:4]## This Step Removes Calorie Information##
    summed_scores = []
    for x in rejigged_scores:
        value = sum(x)
        if value < 0:
            value = 0
        summed_scores.append(value)
    output = 0
    value = math.prod(summed_scores)
    if value > output:
        output = value
    if sum(calories_scores) != 500:
        output = 0
    return output

def ScoreCombinations(ingredients,dict):
    output = 0
    for x in cookie.ratios:
        ratioscore = ScoreRatio(x,ingredients,dict)
        if ratioscore > output:
            output = ratioscore
    return output


def Calculate(inputlines):
    output = 0
    dict = MakeDictionary(inputlines)
    permutations = itertools.permutations(cookie.ingredients)
    for x in permutations:
        combination_score = ScoreCombinations(x,dict)
        if combination_score > output:
            output = combination_score
    return output

cookie = Ingredients()
answer = Calculate(inputlines)
print('Answer is:',answer)