import re

dir = '2015\Day 06\input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def MakeGrid(number0,number1):
    x_list = []
    y_list = []
    off = 0
    for x in range(number1):
        y_list.append(off)
    for x in range(number0):
        x_list.append(y_list)
    return x_list, len(x_list)*len(y_list)

def ExtractInstruction(string):
    output = []
    numbers = re.findall(r'\d+', string)
    output = [[[int(numbers[0]),int(numbers[1])],[int(numbers[2]),int(numbers[3])]]]
    if string.count('turn on') != 0:
        output.append('turnon')
    if string.count('turn off') != 0:
        output.append('turnoff')
    if string.count('toggle') != 0:
        output.append('toggle')
    return output

def ExtractInstructions(list):
    output = []
    for item in list:
        output.append(ExtractInstruction(item))
    return output

def TurnOn(number):
    return number+1

def TurnOff(number):
    return max(0,number-1)

def Toggle(number):
    return number+2

def ApplyRule(number,key):
    if key == 'turnon':
        output = TurnOn(number)
    if key == 'turnoff':
        output = TurnOff(number)
    if key == 'toggle':
        output = Toggle(number)
    return output

def ApplyInstruction(grid,instruction):
    rectangle = instruction[0]
    rule = instruction[1]
    x_lower_edge = min(rectangle[0][0],rectangle[1][0])
    x_upper_edge = max(rectangle[0][0],rectangle[1][0])
    y_lower_edge = min(rectangle[0][1],rectangle[1][1])
    y_upper_edge = max(rectangle[0][1],rectangle[1][1])
    count = 0
    x_list = []    
    for x in range(len(grid)):
        y_list = []
        for y in range(len(grid[x])):
            entry = grid[x][y]
            if y >= y_lower_edge and y <= y_upper_edge and x >= x_lower_edge and x <= x_upper_edge:
                entry = ApplyRule(grid[x][y],rule)
                count += 1
            y_list.append(entry)
        x_list.append(y_list)
    area = (x_upper_edge-x_lower_edge+1)*(y_upper_edge-y_lower_edge+1)
    print(count,"is equal to",area)
    print('0 becomes:',ApplyRule(0,rule))
    print('1 becomes:',ApplyRule(1,rule))
    output = x_list
    return output

def CountLightsBrightness(list_of_lists):
    output = 0
    for list in list_of_lists:
        output += sum(list)
    return output

def ApplyInstructions(grid,instructions):    
    for instruction in instructions:
        print('---Next Instruction---')
        print(instruction)
        print(CountLightsBrightness(grid))
        grid = ApplyInstruction(grid,instruction)
        print(CountLightsBrightness(grid))
    output = grid
    return output

def CountLitLights(list):
    output = 0
    grid, grid_size = MakeGrid(1000,1000)
    instructions = ExtractInstructions(list)
    lights = ApplyInstructions(grid,instructions)
    brightness = CountLightsBrightness(lights)
    output = brightness
    return output

answer = CountLitLights(inputlines)
print("Answer is (in number of lights lit): ",answer)