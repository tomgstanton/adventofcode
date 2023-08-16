import code_part1

dir = '2015\Day 02\input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def SmallSideDimensions(list):
    return sorted(list)[0:2]

def Volume(list):
    output = 1
    for item in list:
        output = output*item
    return output

def FeetRibbon(list):
    output = 0
    for item in list:
        dimensions = code_part1.MakeDimensionsList(item)
        smallside_dimensions = SmallSideDimensions(dimensions)
        smallside_perimeter = 2*sum(smallside_dimensions)
        volume = Volume(dimensions)
        output += smallside_perimeter + volume
    return output

answer = FeetRibbon(inputlines)
print('Answer is (in feet): ',answer)