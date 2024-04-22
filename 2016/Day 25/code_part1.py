dir = '2016/Day 25/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Registers():
    values = {'a':0,'b':0,'c':0,'d':0}
    index = 0

class Instructions():
    list = []

class Transmitter():
    signal = []

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
    if splits[0] == 'out':
        value = Registers.values.get(splits[1])
        if value == None:
            value = splits[1]
        Transmitter.signal.append(value)
  
def Calculate(inputlines):
    for line in inputlines:
        splits = line.split()
        Instructions.list.append(splits)
    a_value = 0
    target = 20
    while len(Transmitter.signal) < target:
        Registers.values['a'] = a_value
        while Registers.index != len(Instructions.list) and len(Transmitter.signal) < target:    
            ReadInstruction(Instructions.list[Registers.index])
            if len(Transmitter.signal) >= 2 and Transmitter.signal[-1] == Transmitter.signal[-2]:
                Transmitter.signal = []
                a_value += 1
                Registers.values = {'a':0,'b':0,'c':0,'d':0}
                Registers.index = 0
                break
            Registers.index += 1 
    return a_value

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)