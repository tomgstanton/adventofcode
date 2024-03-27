dir = '2016/Day 03/input.txt'
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

def TransformTriangles():
    pre_transformation = Triangles.group
    post_transformation = []
    cache_group = []
    while len(pre_transformation) != 0:
        cache_group.append(pre_transformation[0])
        pre_transformation = pre_transformation[1:]
        if len(cache_group) == 3:
            new_triangle_A = [cache_group[0][0],cache_group[1][0],cache_group[2][0]]
            new_triangle_B = [cache_group[0][1],cache_group[1][1],cache_group[2][1]]
            new_triangle_C = [cache_group[0][2],cache_group[1][2],cache_group[2][2]]
            post_transformation.append(new_triangle_A)
            post_transformation.append(new_triangle_B)
            post_transformation.append(new_triangle_C)
            cache_group = []
    Triangles.group = post_transformation

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
    TransformTriangles()
    answer = CountPossibleTriangles()
    return answer        

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)