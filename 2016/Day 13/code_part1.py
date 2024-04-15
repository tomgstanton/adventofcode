dir = '2016/Day 13/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Paths():
    favourite_number = int(inputline)
    visited = [[1,1]]
    possible = [[[1,1]]]

def GetNextSteps(path):
    output = []
    if [path[0]+1,path[1]] not in Paths.visited:
        output.append([path[0]+1,path[1]])
        Paths.visited.append([path[0]+1,path[1]])
    if path[0]-1 >= 0 and [path[0]-1,path[1]] not in Paths.visited:
        output.append([path[0]-1,path[1]])
        Paths.visited.append([path[0]-1,path[1]])
    if [path[0],path[1]+1] not in Paths.visited:
        output.append([path[0],path[1]+1])
        Paths.visited.append([path[0],path[1]+1])
    if path[1]-1 >= 0 and [path[0],path[1]-1] not in Paths.visited:
        output.append([path[0],path[1]-1])
        Paths.visited.append([path[0],path[1]-1])
    return output

def IsWall(coordinates):
    output = False
    coordinate_x = coordinates[0]
    coordinate_y = coordinates[1]
    found_value = (coordinate_x*coordinate_x) + (3*coordinate_x) + (2*coordinate_x*coordinate_y) + coordinate_y + (coordinate_y*coordinate_y)
    favourite_found_value = found_value + Paths.favourite_number
    number_of_one_bits = bin(favourite_found_value)[2:].count('1')
    if number_of_one_bits % 2 != 0:
        output = True
    return output

def CheckForWalls(next_steps):
    output = []
    for step in next_steps:
        if IsWall(step) is False:
            output.append(step)
    return output

def ExtendPaths(path,open_spaces):
    output = []
    for space in open_spaces:
        new_path = path.copy()
        new_path.append(space)
        output.append(new_path)
    return output

def Calculate():
    while True:
        new_paths = []
        for path in Paths.possible:
            possible_next_steps = GetNextSteps(path[-1])
            open_spaces = CheckForWalls(possible_next_steps)
            extended_paths = ExtendPaths(path,open_spaces)
            new_paths += extended_paths
        Paths.possible = new_paths
        for path in Paths.possible:
            if path[-1] == [31,39]:
                return(len(path)-1)
        

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)