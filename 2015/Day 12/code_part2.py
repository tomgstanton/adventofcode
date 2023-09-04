import json
import re

dir = '2015/Day 12/input.txt'
string = open(dir,'r')
inputdict = json.load(string)

class Ignore:
    def __init__(self,):
        self.string = ''
        self.counter = 0

def ExploreList(input0):
    array = input0[:]
    children = []
    memory = []
    while array != []:
        for item in array:
            if array == [] and memory == []:
                break
            if len(memory) != 0 and memory[0] == []:
                memory.remove(memory[0])
            if type(array[0]) is not list:
                children.append(array[0])
                array = array [1:]
            if array != [] and type(array[0]) is list and len(array[0]) == 1:
                children.append(array[0])
                array = array [1:]
            if array != [] and type(array[0]) is list and len(array[0]) > 1:
                memory.append(array[1:])
                array = array[0]
            if array == [] and memory != []:
                array = memory[0]
                memory.remove(memory[0])
    return children

def CheckDict(dictionary):
    deeperlook = []
    for x in dictionary:
        if dictionary[x] == 'red':
            ignore.counter += str(dictionary).count('red')
            ignore.string += str(dictionary)
            deeperlook = []
            break
        if type(dictionary[x]) is list:
            deeperlook += ExploreList(dictionary[x])
        if type(dictionary[x]) is dict:
            deeperlook.append(dictionary[x])
    if deeperlook != []:
        FindReds(deeperlook)

def FindReds(array):
    deeperlook = []
    for x in array:
        if type(x) is dict:
            CheckDict(x)
        if type(x) is list and '{' in str(x) and 'red' in str(x):
            deeperlook += ExploreList(x)
    return deeperlook

def ExtractNumbers(x):
    extracted = re.findall(r'[-+]?\d+',str(x))
    return [int(s) for s in extracted]

def Calculate(inputdict):
    output = 0
    objects = []
    for x in inputdict:
        if str(x)[0] == '[':
            objects += ExploreList(x)
        if str(x)[0] == '{':
            objects.append(x)    
        numbers = ExtractNumbers(x)
        output += sum(numbers)
    furtherobjects = FindReds(objects)
    furthestobjects = FindReds(furtherobjects)
    ignorenumbers = ExtractNumbers(ignore.string)
    ignoresum = sum(ignorenumbers)
    output = output - ignoresum
    return output

ignore = Ignore()
answer = Calculate(inputdict)
print('Answer is:',answer)