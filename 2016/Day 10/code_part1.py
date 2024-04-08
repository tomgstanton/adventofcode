dir = '2016/Day 10/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Robots():
    possession = {}
    instructions = {}
    sought_for = []

def ReadLines(inputlines):
    for line in inputlines:
        splits = line.split()
        target_bot = splits[-2]+' '+splits[-1]
        if Robots.possession.get(target_bot) == None:
            Robots.possession[target_bot] = []
        if splits[0] == 'value':
            Robots.possession[target_bot].append(int(splits[1]))
        else:
            source_bot = splits[0]+' '+splits[1]
            Robots.instructions[source_bot] = [splits[5]+' '+splits[6],target_bot]
            if Robots.possession.get(Robots.instructions[source_bot][0]) == None:
                Robots.possession[Robots.instructions[source_bot][0]] = []

def ApplyInstructions():
    for instruction in Robots.instructions:
        if len(Robots.possession[instruction]) == 2 and min(Robots.possession[instruction]) == 17 and max(Robots.possession[instruction]) == 61:
            Robots.sought_for.append(instruction)
        if len(Robots.possession[instruction]) == 2:
            Robots.possession[Robots.instructions[instruction][0]].append(min(Robots.possession[instruction]))
            Robots.possession[Robots.instructions[instruction][1]].append(max(Robots.possession[instruction]))
            Robots.possession[instruction] = []

def Calculate(inputlines):
    ReadLines(inputlines)
    while Robots.sought_for == []:
        ApplyInstructions()
    return Robots.sought_for[0]

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)