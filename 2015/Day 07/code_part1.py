dir = '2015/Day 07/input.txt'
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
        if x[position] == '1' and y[position] == '1':
            character = '1'
        output += character
    output = int(output,2)
    return output

def FunctionOR(list):
    output = ''
    x = Make16Bit(list[0])
    y = Make16Bit(list[1])
    for position in range(len(x)):
        character = '1'
        if x[position] == '0' and y[position] == '0':
            character = '0'
        output += character
    output = int(output,2)
    return output

def FunctionNOT(list):
    output = ''
    x = Make16Bit(list[0])
    for position in range(len(x)):
        character = '0'
        if x[position] == '0':
            character = '1'
        output += character
    output = int(output,2)
    return output

def FunctionRSHIFT(list):
    output = ''
    x = Make16Bit(list[0])
    y = int(list[1])
    value = x
    for number in range(y):
        value = '0'+value
        value = value[:-1]
    output = int(value,2)
    return output

def FunctionLSHIFT(list):
    output = ''
    x = Make16Bit(list[0])
    y = int(list[1])
    value = x
    for number in range(y):
        value = value+'0'
        value = value[1:]
    output = int(value,2)
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
    for item in dict['inputs']:
        try:
            int(item)
            check.append('pass')
        except:
            check.append(CheckDict(item))
    if 'fail' in check:
        output = False
    return output

def ApplyFunction(item):
    value = None
    inputs = []
    for element in item['inputs']:
        number = element
        try:
            number = Values.values[element]
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
    Values.values[item['output']] = value    

def Apply(list):
    for item in list:
        if CheckInputs(item) == True and Values.values[item['output']] == None:             
            ApplyFunction(item)    

def Calculate(lines):    
    instructions = ExtractInstructions(lines)
    while CountUnknownValues() != 0:
        Apply(instructions)

Values = ValuesDict()
Calculate(inputlines)

results = ['a']
for result in results:
    print('Answer is:',result,'=',Values.values[result])