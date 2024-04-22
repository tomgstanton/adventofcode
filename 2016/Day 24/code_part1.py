dir = '2016/Day 24/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Memory():
    map = inputlines
    characters = ['0','1','2','3','4','5','6','7']
    targets = {}
    part_paths = {}

def ReadMap():
    for line in Memory.map:
        clean_line = line
        if line[-1] == '\n':
            clean_line = line[:-1]
        for char in clean_line:
            if char in Memory.characters:
                Memory.targets[char] = [clean_line.index(char),Memory.map.index(line)]
                Memory.part_paths[char] = {'found':0}

def GetPotentialMoves(start_locations):
    output = []
    for location in start_locations:
        if [location[0]+1,location[1]] not in output:
            output.append([location[0]+1,location[1]])
        if [location[0]-1,location[1]] not in output:
            output.append([location[0]-1,location[1]])
        if [location[0],location[1]+1] not in output:
            output.append([location[0],location[1]+1])
        if [location[0],location[1]-1] not in output:
            output.append([location[0],location[1]-1])
    return output

def Explore(char):
    start_locations = [Memory.targets[char]]
    new_map = Memory.map.copy()
    steps = 0
    for line in new_map:
        clean_line = line
        if line[-1] == '\n':
            clean_line = line[:-1]
        print(clean_line)
    while Memory.part_paths[char].get('found') != 7:
        potential_moves = GetPotentialMoves(start_locations)
        start_locations = []
        for move in potential_moves:
            if new_map[move[1]][move[0]] != '#' and new_map[move[1]][move[0]] != char:
                if new_map[move[1]][move[0]] != '.':
                    Memory.part_paths[char][new_map[move[1]][move[0]]] = steps+1
                    Memory.part_paths[char]['found'] += 1
                new_map[move[1]] = new_map[move[1]][:move[0]]+char+new_map[move[1]][move[0]+1:]
                start_locations.append(move)
        for line in new_map:
            clean_line = line
            if line[-1] == '\n':
                clean_line = line[:-1]
            print(clean_line)
        steps += 1

def ShortestPath():
    output = 0
    characters = Memory.characters
    source_char = '0'
    characters.remove(source_char)
    while characters != []:
        shortest_distance = 999
        for char in characters:
            distance = Memory.part_paths[source_char].get(char)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_char = char
        source_char = nearest_char
        characters.remove(source_char)
        output += shortest_distance
    return output

def Calculate():
    ReadMap()
    for char in Memory.characters:
        Explore(char)
    return ShortestPath()

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)