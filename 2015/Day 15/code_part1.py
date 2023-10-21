import itertools
import math

dir = '2015/Day 15/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Ingredients():
    def __init__(self,):
        self.ingredients = []

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

def Calculate(inputlines):
    dict = MakeDictionary(inputlines)
    permutations = itertools.permutations(cookie.ingredients)
    #for x in permutations:
    #    print(x)
    return 'testing'

cookie = Ingredients()
#answer = Calculate(inputlines)
#print('Answer is:',answer)

grand_total = 100

def GetNumbers(quantity,maximum,number):
    output = []
    count = min(quantity,maximum)
    for x in range(quantity):
        #print(count)
        output.append(count)
        if count == math.ceil(quantity/number):
            break
        count -= 1
    return output

def Function(quantity,number):
    output = []
    temp0 = GetNumbers(quantity,100,number)
    #print(temp0)
    for x in temp0:
        #print(x)
        new_quant = grand_total-x
        temp1 = GetNumbers(new_quant,x,number-1)
        #print(temp1)
        for y in temp1:
            new_quant = grand_total-x-y
            temp2 = GetNumbers(new_quant,y,number-2)
            #print(temp2)
            for z in temp2:
                new_quant = grand_total-x-y-z
                temp3 = GetNumbers(new_quant,z,number-3)
                #print(temp3)
                for a in temp3:
                    output.append([x,y,z,a])
    return output

starting_total = 100

def GetNumbers0(list,maximum,number):
    output = []
    quantity = sum(list)
    count = min(quantity,maximum)
    for x in range(quantity):
        temp_set = []
        temp_set.append(x)
        if sum(temp_set) != starting_total:
            results = GetNumbers0(temp_set,x,number-1)
            print(results)
        #print(count)
        output.append(count)
        if count == math.ceil(quantity/number):
            break
        count -= 1
    return output

def Function0(quantity,number):
    output = []
    starting_total = quantity
    output = GetNumbers0([quantity],quantity,number)
    print(output)

Function0(100,4)

#ratios = Function(100,4)
#total = []
#for x in ratios:
#    print(x,sum(x))
#    if sum(x) not in total:
#        total.append(sum(x))
#print(total)