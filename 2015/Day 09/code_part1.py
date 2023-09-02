import itertools

dir = '2015/Day 09/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Locations:
    def __init__(self,):
        self.locations = []
        self.functions = []

def LoadLocations(line):
    pair = [line.split()[0],line.split()[2]]
    distance = line.split()[4]
    for x in pair:
        if x not in cities.locations:
            cities.locations.append(x)
    set_pair = {pair[0],pair[1]}
    cities.functions.append([set_pair,distance])

def GetDistance(set_pair):
    for function in cities.functions:
        if set_pair == function[0]:
            return function[1]

def MeasurePath(x,output,oldpath):
    path_length = 0
    newpath = []
    for index in range(len(x)):
        if index != 0:
            set_pair = {x[index-1],x[index]}
            distance = GetDistance(set_pair)
            path_length += int(distance)
            newpath.append([set_pair,distance])
    if path_length > output:
        return output, oldpath
    return path_length, newpath

def Calculate():
    output = 1000000
    path = []
    for line in inputlines:
        LoadLocations(line)
    permutations = itertools.permutations(cities.locations)
    for x in permutations:
        output, path = MeasurePath(x,output,path)
    return output, path

cities = Locations()
answer, path = Calculate()
print('Answer is:',answer)
print('Answer with workings:',path)

