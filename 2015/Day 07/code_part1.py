import re

dir = '2015\Day 07\input.txt'
string = open(dir,'r')
inputlines = string.readlines()

functions = ['AND','OR','NOT','LSHIFT','RSHIFT']

class ValuesDict:
    def __init__(self,):
        self.values = {}

def MakeDictEntry(string):
    Values.values[string] = None

def ExtractInstruction(string):
    output = {
        'inputs':[],
        'function': None,
        'output':'character'
    }
    words = string.split()
    for function in functions:
        if string.count(function) != 0:
            output['function'] = function
    output['output'] = words[-1]
    for item in [output['function'],'->',output['output']]:
        if item != None:
            words.remove(item)
    output['inputs'] = words
    MakeDictEntry(output['output'])
    return output

def ExtractInstructions(list):
    output = []
    for item in list:
        output.append(ExtractInstruction(item))
    return output

def Make16Bit(number):
    integer = int(number)
    output = str(bin(integer))
    output = output[2:].zfill(16)
    return(output)

def FunctionAND(list):
    output = ''
    x = Make16Bit(list[0])
    y = Make16Bit(list[1])
    for position in range(len(x)):
        character = '0'
        if x[position] == '1' and y[position] == '1':  #Maybe remove quotes#
            character = '1'
        output += character
    output = int(output,2)
    return output

def FunctionOR(list):
    output = ''
    x = Make16Bit(list[0])
    y = Make16Bit(list[1])
    for position in range(len(x)):
        character = '0'
        if x[position] == '1' or y[position] == '1':  #Maybe remove quotes#
            character = '1'
        output += character
    output = int(output,2)
    return output

def FunctionNOT(list):
    output = ''
    x = Make16Bit(list[0])
    for position in range(len(x)):
        character = '0'
        if x[position] == '0':  #Maybe remove quotes#
            character = '1'
        output += character
    output = int(output,2)
    return output

def FunctionRSHIFT(list):
    output = ''
    x = Make16Bit(list[0])
    y = int(list[1])
    for position in range(len(x)):
        character = x[position-y]
        output += character
    output = int(output,2)
    return output

def FunctionLSHIFT(list):
    output = ''
    x = Make16Bit(list[0])
    y = int(list[1])
    for position in range(len(x)):
        character = x[position-(len(x)-y)]
        output += character
    output = int(output,2)
    return output

def CountUnknownValues():
    output = 0
    for key in Values.values:
        if Values.values[key] == None:
            output += 1
    return output

def CheckDict(string):
    output = 'pass'
    if Values.values[string] == None:
        output = 'fail'
    return output

def CheckInputs(dict):
    output = True
    check =[]
    #print(dict['inputs'])
    for item in dict['inputs']:
        try:
            int(item)
            check.append('pass')
            #print('integar',item)
        except:
            #print('nonintegar',item)
            check.append(CheckDict(item))
    if 'fail' in check:
        output = False
    return output

def ApplyFunction(item):
    value = None
    inputs = []
    for input in item['inputs']:
        number = input
        try:
            number = Values.values[input]
        except:
            None
        inputs.append(number)
    if item['function'] == None:
        value = inputs[0]
    if item['function'] == 'AND':
        value = FunctionAND(inputs)
    if item['function'] == 'OR':
        value = FunctionOR(inputs)
    if item['function'] == 'NOT':
        value = FunctionNOT(inputs)
    if item['function'] == 'LSHIFT':
        value = FunctionLSHIFT(inputs)
    if item['function'] == 'RSHIFT':
        value = FunctionRSHIFT(inputs)
    print(inputs,item['function'])
    print(item['output'],Values.values[item['output']],value)
    Values.values[item['output']] = value

def Apply(list):
    for item in list:
        if CheckInputs(item) == True and Values.values[item['output']] == None:             
            ApplyFunction(item)    

def FindValueByKey(string):
    output = Values.values[string] 
    return output  

def Calculate(key):    
    instructions = ExtractInstructions(inputlines)
    while CountUnknownValues() != 0:
        print('unknown values:',CountUnknownValues())
        Apply(instructions)
        print('not finished')
    output = FindValueByKey(key)
    return output

Values = ValuesDict()
answer = Calculate('a')

print('Answer is: \'a\' =',answer)
#print(Values.values)

#Values = ValuesDict()
#ExtractInstructions(inputlines)
#print(FunctionAND([49150, 54125]))#37740
#print(FunctionOR([98,1]))#99
#print(FunctionLSHIFT([1,'15']))#32768
#print(FunctionRSHIFT([61355,2]))#64490
#print(FunctionNOT([23925]))#41610
#print(FunctionNOT([456]))
#print(123)
#print(456)