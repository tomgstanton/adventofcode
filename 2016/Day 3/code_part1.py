dir = '2016/Day 3/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Triangles():
    group = []

def ReadInput(inputlines):
    group = []
    for line in inputlines:
        splits = line.split()
        group.append(splits)
    for triangle in group:
        cleaned_triangle = []
        for number in triangle:
            cleaned_triangle.append(int(number))
        Triangles.group.append(cleaned_triangle)

def Possible(triangle):
    output = False
    min_length = min(triangle)
    max_length = max(triangle)
    total_lengths = sum(triangle)
    mid_length = total_lengths - min_length - max_length
    if min_length + mid_length > max_length:
        output = True
    return output

def CountPossibleTriangles():
    output = 0
    for triangle in Triangles.group:
        if Possible(triangle) == True:
            output += 1
    return output

def Calculate(inputlines):
    ReadInput(inputlines)
    answer = CountPossibleTriangles()
    return answer        

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)