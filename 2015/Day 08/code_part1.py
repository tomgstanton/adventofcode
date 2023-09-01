dir = '2015/Day 08/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Counts():
    def __init__(self,):
        self.string_literals = 0
        self.string_memories = 0

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

def KnockQuotesOff(string):
    return string[1:-1]

def AddMemoryCount(string):
    string = KnockQuotesOff(string)
    memory_string = ''
    ignore_chars = 0
    for char in range(len(string)):
        if ignore_chars == 0 and string[char:char+2] in ['\\\\','\\\"']:
            ignore_chars = 2
        if ignore_chars == 0 and string[char:char+2] == '\\x' and CheckHex(string[char+2:char+4]) == True:
            ignore_chars = 4
        ignore_chars = max(0,ignore_chars-1)
        if ignore_chars == 0:
            memory_string = memory_string + string[char]        
    count.string_memories += len(memory_string) 

def AddCounts(string): 
    string = string.replace('\n','')       
    AddLiteralCount(string)    
    AddMemoryCount(string)

def Calculate(inputlines):
    for line in inputlines:
        AddCounts(line)
    return count.string_literals - count.string_memories

count = Counts()
answer = Calculate(inputlines)
print('Answer is: ',answer)
