dir = '2015/Day 11/input.txt'
string = open(dir,'r')
inputline = string.read()

alphabet = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'] 

def ConditionOne(string):
    output = False
    for index in range(len(string)-2):
        first_index = alphabet.index(string[index])
        second_index = alphabet.index(string[index+1])
        third_index = alphabet.index(string[index+2])
        if third_index == second_index-1 and second_index == first_index-1:
            output = True
    return output

def ConditionTwo(string):
    output = False
    for x in ['i','o','l']:
        if x in string:
            output = True
    return output

def ConditionThree(string):
    output = False
    pairs = []
    for index in range(len(string)-1):
        if string[index] == string[index+1]:
            pairs.append(string[index]+string[index])
    if len(set(pairs)) >= 2:
        output = True
    return output

def CheckValid(string):
    output = True
    if ConditionOne(string) == False:
        output = False
    if ConditionTwo(string) == True:
        output = False
    if ConditionThree(string) == False:
        output = False
    return output

def Increment(line):      
    place = -1
    output = [x for x in line]           
    output[place] = alphabet[alphabet.index(output[place])-1]
    if output[-1] == alphabet[-1]:
        resolve = False
        for index in range(len(output)-1):
            if output[-index-1] == alphabet[-1] and resolve == False:
                output[-index-2] = alphabet[alphabet.index(output[-index-2])-1]
                if output[-index-2] != alphabet[-1]:
                    resolve = True
    output = ''.join(output)
    return output

def Calculate(line):
    line = Increment(line)
    while CheckValid(line) == False:
        line = Increment(line)
    return line

answer = Calculate(inputline)
print('Answer is:',answer)