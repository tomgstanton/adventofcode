import code_part1

dir = '2015\Day 05\input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def CountPairs(string):
    output = 0
    for x in range(len(string)):
        if x != 0 and string[x+1:].count(string[x-1:x+1]) != 0:
            output += 1
            break
    return output

def SpacedLetters(string):
    output = 0
    for x in range(len(string)):
        if x > 1 and string[x-2] == string[x]:
            output += 1
            break
    return output

def CheckNiceness(string):
    output = True
    number_of_distinct_pairs = CountPairs(string)
    if number_of_distinct_pairs == 0:
        output = False
    spaced_letters = SpacedLetters(string)
    if spaced_letters == 0:
        output = False
    return output

def CountNices(list):
    output = 0
    for item in list:
        if CheckNiceness(item) == True:
            output += 1
    return output

answer = CountNices(inputlines)
print("Answer is (in nices): ",answer)