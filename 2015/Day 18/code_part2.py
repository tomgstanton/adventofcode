import re

dir = '2015/Day 18/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

testing_set = ['.#.#.#','...##.','#....#','..#...','#.#..#','####..']

def MakeDictionary(sample_set):
    output = {}
    y_number = len(sample_set)
    line = sample_set[0].replace('\n','')
    x_number = len(line)
    for y in range(y_number):
        for x in range(x_number):
            item_name = str([x,y])
            output[item_name] = sample_set[y][x]
    for item_name in [str([0,0]),str([0,99]),str([99,0]),str([99,99])]:
        output[item_name] = '#'
    return output

def Adjustments():
    output = []
    values = [-1,0,1]
    for a in values:
        for b in values:
            output.append([a,b])
    return output

def TestValues(list_values):
    starting_value = list_values[4]
    on_counts = list_values.count('#')
    new_value = '.'
    if starting_value == '#' and on_counts in [3,4]:
        new_value = '#'
    if starting_value == '.' and on_counts == 3:
        new_value = '#'
    return new_value

def RunChanges(dictionary,adjustments):
    output = {}
    for x in dictionary:
        values = []
        for y in adjustments:
            elements = re.findall(r'\d+', x)
            xh = [int(a) for a in elements]
            item_name = [a+b for a,b in zip(xh,y)]
            value = dictionary.get(str(item_name))
            if value == None:
                value = '.'
            values.append(value)
        value = TestValues(values)
        output[x] = value
        if x in [str([0,0]),str([0,99]),str([99,0]),str([99,99])]:
            output[x] = '#'
    return output

def CountOnLights(dictionary):
    output = 0
    for x in dictionary:
        value = dictionary[x]
        if value == '#':
            output += 1
    return output

def Calculate(lines):
    dictionary = MakeDictionary(lines)
    adjustments = Adjustments()
    iteration = 0
    target = 100
    while iteration != target:
        dictionary = RunChanges(dictionary,adjustments)
        iteration += 1
    output = CountOnLights(dictionary)
    return output

answer = Calculate(inputlines)
print('Answer is:',answer)