import hashlib

dir = '2016/Day 17/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Memory():
    passcode = inputline
    directions_order = ['U','D','L','R']
    paths = ['']
    shortest_path = ''

def DoorStatus(char):
    output = 'closed and locked'
    if char in ['b','c','d','e','f']:
        output = 'open'
    return output

def GetOpenDirections():
    open_directions = []
    for path in Memory.paths:
        string = Memory.passcode+path
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()    
        for direction in Memory.directions_order:
            if DoorStatus(hash[Memory.directions_order.index(direction)]) == 'open':
                open_directions.append(path+direction)
    return open_directions

def CheckForWalls(paths):
    valid_paths = paths
    for path in paths:
        location = [0,0]
        for direction in path:
            if direction == 'U':
                location[1] -= 1
            if direction == 'D':
                location[1] += 1
            if direction == 'L':
                location[0] -= 1
            if direction == 'R':
                location[0] += 1
            if -1 in location or 4 in location:
                valid_paths.remove(path)
            if location == [3,3]:
                Memory.shortest_path = path
    Memory.paths = valid_paths

def Calculate():
    while Memory.shortest_path == '':
        open_directions = GetOpenDirections()
        CheckForWalls(open_directions)
    return Memory.shortest_path
    
if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)