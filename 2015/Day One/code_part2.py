import code_part1
dir = '2015\Day One\input.txt'
string = open(dir,'r')
inputstring = string.read()

def FirstBasement(string):
    for x in range(len(string)):
        substring = string[0:x]
        floor = code_part1.FinalFloor(substring)
        if floor < 0:
            output = len(substring)
            print('Basement Reached. Instruction Number: ',output)
            break
    return output

answer = FirstBasement(inputstring)
