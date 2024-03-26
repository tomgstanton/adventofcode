dir = '2016/Day 1/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Instructions():
    starting_location = [0,0]
    facing_direction = 'N'
    direction_list = ['N','E','S','W']
    current_location = [0,0]
    instructions = []

def Apply(instruction):
    current_index = Instructions.direction_list.index(Instructions.facing_direction)
    if instruction[0] == 'R':
        new_index = current_index+1
        if new_index == 4:
            new_index = 0
        Instructions.facing_direction = Instructions.direction_list[new_index]
    if instruction[0] == 'L':
        new_index = current_index-1
        Instructions.facing_direction = Instructions.direction_list[new_index]
    for direction in Instructions.direction_list:
        if direction == Instructions.facing_direction and direction == 'N':
            Instructions.current_location[1] += instruction[1]
        if direction == Instructions.facing_direction and direction == 'E':
            Instructions.current_location[0] += instruction[1]
        if direction == Instructions.facing_direction and direction == 'S':
            Instructions.current_location[1] -= instruction[1]
        if direction == Instructions.facing_direction and direction == 'W':
            Instructions.current_location[0] -= instruction[1]

def Calculate(inputline):
    splits = inputline.split()
    for split in splits:
        if split[-1] == ',':
            split = split[:-1]
        Instructions.instructions.append([split[0],int(split[1:])])
    for instruction in Instructions.instructions:
        Apply(instruction)
    return sum(abs(number) for number in Instructions.current_location)
        
if __name__ == '__main__':
    answer = Calculate(inputline)
    print('Answer is:',answer)