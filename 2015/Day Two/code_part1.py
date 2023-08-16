dir = '2015\Day Two\input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def MakeDimensionsList(string):
    output = []
    length = string[0:string.index('x')]
    string = string[string.index('x')+1:]
    width = string[0:string.index('x')]
    string = string[string.index('x')+1:]
    height = string.replace('\n','')
    output.append(int(length))
    output.append(int(width))
    output.append(int(height))
    return output

def PaperNeeded(list):
    sides = [x*y for x in list for y in list]
    for item in list:
        sides.remove(item**2)
    sides.append(min(sides))
    output = sum(sides)
    return output

def SquareFeetPaper(list):
    output = 0
    for item in list:
        dimensions = MakeDimensionsList(item)
        output += PaperNeeded(dimensions)
    return output

answer = SquareFeetPaper(inputlines)
print('Answer is (in square feet): ',answer)