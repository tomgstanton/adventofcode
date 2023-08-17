dir = '2015\Day 05\input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def CountVowels(string):
    vowels = ['a','e','i','o','u']
    tally = []
    for vowel in vowels:
        tally.append(string.count(vowel))
    vowelcount = sum(tally)
    return vowelcount

def DoubledLetters(string):
    output = 0
    for x in range(len(string)):
        if x != 0 and string[x-1] == string[x]:
            output += 1
    return output

def ForbiddenSubstrings(string):
    output = 0
    forbidden_list = ['ab','cd','pq','xy']
    for item in forbidden_list:
        output += string.count(item)
    return output

def CheckNiceness(string):
    output = True
    number_of_vowels = CountVowels(string)
    if number_of_vowels < 3:
        output = False
    doubled_letters = DoubledLetters(string)
    if doubled_letters == 0:
        output = False
    forbidden_substrings = ForbiddenSubstrings(string)
    if forbidden_substrings != 0:
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