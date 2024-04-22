dir = '2016/Day 23/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Registers():
    values = {'a':12,'b':0,'c':0,'d':0}
    index = 0

class Instructions():
    list = []

def ReadInstruction(splits):
    print(Registers.values)
    if splits[0] == 'cpy':        
        entry_value = Registers.values.get(splits[1])
        if entry_value == None:
            entry_value = int(splits[1])
        Registers.values[splits[2]] = entry_value
    if splits[0] == 'inc' and splits[1] != 'a':
        Registers.values[splits[1]] += 1
    if splits[0] == 'inc' and splits[1] == 'a':###
        Registers.values[splits[1]] += Registers.values['c']*Registers.values['d']###
        Registers.values['c'] = 1###
        Registers.values['d'] = 1###
    if splits[0] == 'dec':
        Registers.values[splits[1]] -= 1
    if splits[0] == 'jnz':
        entry_value = Registers.values.get(splits[1])
        if entry_value == None:
            entry_value = int(splits[1])
        if entry_value != 0:
            entry_value = Registers.values.get(splits[2])
            if entry_value == None:
                entry_value = int(splits[2])
            Registers.index += entry_value-1
    if splits[0] == 'tgl':
        toggled_index = Registers.index+Registers.values.get(splits[1])
        if toggled_index < len(Instructions.list):
            if len(Instructions.list[toggled_index]) == 2:
                if Instructions.list[toggled_index][0] == 'inc':
                    Instructions.list[toggled_index][0] = 'dec'
                else:
                    Instructions.list[toggled_index][0] = 'inc'
            if len(Instructions.list[toggled_index]) == 3:
                if Instructions.list[toggled_index][0] == 'jnz':
                    Instructions.list[toggled_index][0] = 'cpy'
                else:
                    Instructions.list[toggled_index][0] = 'jnz'

def Calculate(inputlines):
    for line in inputlines:
        splits = line.split()
        Instructions.list.append(splits)
    while Registers.index != len(Instructions.list):       
        ReadInstruction(Instructions.list[Registers.index])
        Registers.index += 1
    return Registers.values['a']

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)