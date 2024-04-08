dir = '2016/Day 12/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Registers():
    values = {'a':0,'b':0,'c':1,'d':0}
    index = 0

def ReadInstruction(splits):
    if splits[0] == 'cpy':
        entry_value = Registers.values.get(splits[1])
        if entry_value == None:
            entry_value = int(splits[1])
        Registers.values[splits[2]] = entry_value
    if splits[0] == 'inc':
        Registers.values[splits[1]] += 1
    if splits[0] == 'dec':
        Registers.values[splits[1]] -= 1
    if splits[0] == 'jnz':
        entry_value = Registers.values.get(splits[1])
        if entry_value == None:
            entry_value = int(splits[1])
        if entry_value != 0:
            Registers.index += int(splits[2])-1

def Calculate(inputlines):
    instructions = []
    for line in inputlines:
        splits = line.split()
        instructions.append(splits)
    while Registers.index != len(instructions):       
        ReadInstruction(instructions[Registers.index])
        Registers.index += 1
    return Registers.values['a']

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)