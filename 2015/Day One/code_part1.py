dir = '2015\Day One\input.txt'
string = open(dir,'r')
inputstring = string.read()

def FinalFloor(string):
    total_instructions = len(string)
    up_instructions = string.count('(')
    down_instructions = string.count(')')
    output = up_instructions - down_instructions
    print('Number of Instructions: ', total_instructions)
    print('Number of Up Instructions: ', up_instructions)
    print('Number of Down Instructions: ', down_instructions)
    print('Final Floor: ', output)
    return output

answer = FinalFloor(inputstring)
