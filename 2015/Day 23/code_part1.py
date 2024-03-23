dir = '2015/Day 23/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Registers:
    a = 0
    b = 0

def MakeListOfInstructions(inputlines):
    output = []
    for line in inputlines:
        splits = line.split()
        for part in splits:
            if part[-1] == ',':
                splits[splits.index(part)] = part[:-1]
        output.append(splits)
    return output

def Apply(instructions):
    index = 0
    while index in range(len(instructions)):        
        print('A:',Registers.a,', B:',Registers.b)
        print('Instruction:',index,instructions[index])
        jump = 1
        if instructions[index][1] == 'a':
            register = Registers.a
        if instructions[index][1] == 'b':
            register = Registers.b
        if instructions[index][0] == 'hlf':
            register = int(register / 2)
        if instructions[index][0] == 'tpl':
            register = int(register * 3)
        if instructions[index][0] == 'inc':
            register += 1
        if instructions[index][0] == 'jmp':
            jump = int(instructions[index][1])
        if instructions[index][0] == 'jie' and register % 2 == 0:
            jump = int(instructions[index][2])
        if instructions[index][0] == 'jio' and register == 1:
            jump = int(instructions[index][2])
        if instructions[index][1] == 'a':
            Registers.a = register
        if instructions[index][1] == 'b':
            Registers.b = register
        index += jump
        print('A:',Registers.a,', B:',Registers.b)
        # input()

def Calculate(inputlines):
    instructions = MakeListOfInstructions(inputlines)
    Apply(instructions)
    return Registers.b

if __name__ == '__main__':
    register = Registers()
    answer = Calculate(inputlines)
    print('Answer is:',answer)