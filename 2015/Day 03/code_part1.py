dir = '2015\Day 03\input.txt'
string = open(dir,'r')
inputstring = string.read()

dict = {'^':[0,1],
    '>':[1,0],
    'v':[0,-1],
    '<':[-1,0]}

def DecodeMovement(character):
    output = dict[character]
    return output

def RemoveDuplicates(list):
    output = []
    for entry in list:
        if entry not in output:
            output.append(entry)
    return output

def HouseCounter(string):
    output = []
    location = [0,0]
    for character in string:
        movement = DecodeMovement(character)
        location = [x+y for x,y in zip(location,movement)]
        output.append(location)
    return output

houses = HouseCounter(inputstring)
houses = RemoveDuplicates(houses)
answer = len(houses)
print('Answer is (in houses): ',answer)