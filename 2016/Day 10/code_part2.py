dir = '2016/Day 10/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Robots():
    possession = {}
    instructions = {}

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
        if len(Robots.possession[instruction]) == 2:
            Robots.possession[Robots.instructions[instruction][0]].append(min(Robots.possession[instruction]))
            Robots.possession[Robots.instructions[instruction][1]].append(max(Robots.possession[instruction]))
            Robots.possession[instruction] = []

def CheckActiveRobots():
    output = False
    for possession in Robots.possession:
        if len(Robots.possession[possession]) == 2:
            output = True
    return output

def Calculate(inputlines):
    ReadLines(inputlines)
    while CheckActiveRobots() == True:
        ApplyInstructions()
    return Robots.possession['output 0'][0] * Robots.possession['output 1'][0] * Robots.possession['output 2'][0]

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)