import json
import re

dir = '2015/Day 12/input.txt'
string = open(dir,'r')
inputdict = json.load(string)

def ExtractNumbers(x):
    extracted = re.findall(r'[-+]?\d+',str(x))
    return [int(s) for s in extracted]

def Calculate(inputdict):
    output = 0
    for x in inputdict:
        numbers = ExtractNumbers(x)
        output += sum(numbers)
    return output

answer = Calculate(inputdict)
print('Answer is:',answer)