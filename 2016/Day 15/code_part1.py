dir = '2016/Day 15/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Memory():
    time = 0
    disks = {}
    streak = 0

def Positions(number_of_positions,starting_position):
    output = []
    number = 0
    for x in range(number_of_positions):
        output.append(number)
        number += 1
    while output[0] != starting_position:
        output = [output[-1]]+output[:-1]
    return output

def Tick():
    for disk in Memory.disks:
        Memory.disks[disk] = Memory.disks[disk][1:]+[Memory.disks[disk][0]]
    if Memory.disks[Memory.streak+1][0] == 0:
        Memory.streak += 1
    else:
        Memory.streak = 0
    Memory.time += 1

def Calculate(inputlines):
    for line in inputlines:
        splits = line.split()
        disk = int(splits[1][-1])
        Memory.disks[disk] = Positions(int(splits[3]),int(splits[-1][:-1]))
    while Memory.streak != len(Memory.disks):
        Tick()
    return Memory.time-len(Memory.disks)

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)