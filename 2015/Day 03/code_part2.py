import code_part1

dir = '2015\Day 03\input.txt'
string = open(dir,'r')
inputstring = string.read()

dict = {'^':[0,1],
    '>':[1,0],
    'v':[0,-1],
    '<':[-1,0]}

def AlternateInstructions(string):
    output0 = ''
    output1 = ''
    for character in string:
        if len(output0) == len(output1):
            output0 += character
        else:
            output1 += character
    return output0, output1

santastring, robosantastring = AlternateInstructions(inputstring)

santahouses = code_part1.HouseCounter(santastring)
robosantahouses = code_part1.HouseCounter(robosantastring)
houses = []
for house in santahouses:
    houses.append(house)
for house in robosantahouses:
    houses.append(house)
houses = code_part1.RemoveDuplicates(houses)
answer = len(houses)
print('Answer is (in houses): ',answer)