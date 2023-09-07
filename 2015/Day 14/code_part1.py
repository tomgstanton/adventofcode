import re

dir = '2015/Day 14/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def ExtractNumbers(x):
    extracted = re.findall(r'[-+]?\d+',str(x))
    return [int(s) for s in extracted]

def StartRace(numbers,time_limit):
    template = numbers[:]
    distance = 0
    second = 1
    while second != time_limit+1: 
        if template[1] == 0 and template[3] != 0:
            distance += template[2]
            template[3] -= 1
        if template[1] != 0:
            distance += template[0]
            template[1] -= 1
        if template[1] == 0 and template[1] == template[3]:
            template = numbers[:]
        second += 1
    return distance

def Calculate(lines,time_limit):
    output = 0
    for line in lines:
        numbers = ExtractNumbers(line)
        numbers.insert(2,0)
        distance = StartRace(numbers,time_limit)
        if distance > output:
            output = distance
    return output

answer = Calculate(inputlines,2503)
print('Answer is:',answer)