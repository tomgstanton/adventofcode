import code_part1

dir = '2015/Day 08/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Counts():
    def __init__(self,):
        self.string_literals = 0
        self.string_memories = 0
        self.string_encoded = 0

def AddLiteralCount(string):
    tally = 0
    for x in string:
        tally += 1
    count.string_literals += tally

def CheckHex(string):
    output = True
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for char in string:
        if char not in hex_digits:
            output = False
    return output

def WrapInQuotes(string):
    return '\"'+string+'\"'

def AddEncodedCount(string):
    encoded = ''
    for char in range(len(string)):
        nextchar = string[char]
        if string[char] in ['\\','"']:
            nextchar = '\\'+string[char]
        if string[char] == '\\' and string[char+1] == 'x' and CheckHex(string[char+1:char+3]) == True:
            nextchar = '"\\\\"'+string[char]
        encoded += nextchar
    encoded = WrapInQuotes(encoded)
    count.string_encoded += len(encoded)

def AddCounts(string): 
    string = string.replace('\n','')       
    AddLiteralCount(string)    
    AddEncodedCount(string)

def Calculate(inputlines):
    for line in inputlines:
        AddCounts(line)
    return count.string_encoded - count.string_literals

count = Counts()
answer = Calculate(inputlines)
print('Answer is: ',answer)
