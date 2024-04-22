dir = '2016/Day 22/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Memory():
    data = inputlines
    nodes = []
    nonempty_nodes = []
    viable_pairs = []
    capacious_nodes = []

def ReadData():
    for line in Memory.data:
        if line[-1] == '\n':
            line = line[:-1]
        splits = line.split()
        if '-' in splits[0]:
            splits[0] = splits[0].split('-')
        if line[0] == '/':
            entry = {'x-axis':int(splits[0][1][1:]),'y-axis':int(splits[0][2][1:]),'size':int(splits[1][:-1]),'used':int(splits[2][:-1]),'avail':int(splits[3][:-1])}
            Memory.nodes.append(entry)
            if entry['used'] != 0:
                Memory.nonempty_nodes.append(entry)

def GetViablePairs():
    for node_A in Memory.nonempty_nodes:
        for node_B in Memory.nodes:
            if node_A != node_B and node_A['used'] <= node_B['avail']:
                Memory.viable_pairs.append([node_A,node_B])
                if node_B not in Memory.capacious_nodes:
                    Memory.capacious_nodes.append(node_B)

def GiveNames():
    for node in Memory.nodes:
        name = '.'
        if node == Memory.capacious_nodes[0]:
            name = '_'
        if node['used'] > Memory.capacious_nodes[0]['avail']:
            name = '#'
        if node['x-axis'] == 29 and node['y-axis'] == 0:
            name = 'G'
        node['name'] = name

def Locate(name):
    if name == '#':
        output = []
        for node in Memory.nodes:
            if node.get('name') == name:
                output.append([node['x-axis'],node['y-axis']])
        return output
    for node in Memory.nodes:
        if node.get('name') == name:
            return [node['x-axis'],node['y-axis']]
        
def Move(direction):
    for node in Memory.nodes:
        if node.get('x-axis') == direction[0] and node.get('y-axis') == direction[1]:
            used_data = node['used']
            name_data = node['name']
            node['avail'] += used_data
            node['used'] = 0
            node['name'] = '_'            
            Memory.nodes[Memory.nodes.index(Memory.capacious_nodes[0])]['used'] = used_data
            Memory.nodes[Memory.nodes.index(Memory.capacious_nodes[0])]['avail'] -= used_data
            Memory.nodes[Memory.nodes.index(Memory.capacious_nodes[0])]['name'] = name_data            
            Memory.capacious_nodes[0] = node

def Calculate():
    ReadData()
    GetViablePairs()
    GiveNames()
    move_count = 0
    while Locate('G') != [0,0]:
        goal_location = Locate('G')
        goal_x = goal_location[0]
        goal_y = goal_location[1]
        space_location = Locate('_')  
        space_x = space_location[0]
        space_y = space_location[1]
        full_nodes = Locate('#')
        if space_x < goal_x and space_y > goal_y:
            new_location = [space_x,space_y-1]
            if new_location in full_nodes:
                new_location = [space_x-1,space_y]
            Move(new_location)
        if space_x < goal_x and space_y == goal_y:
            new_location = [space_x+1,space_y]
            Move(new_location)
        if space_x > goal_x and space_y == goal_y:
            new_location = [space_x,space_y+1]
            Move(new_location)
        if space_x >= goal_x and space_y == goal_y+1:
            new_location = [space_x-1,space_y]
            Move(new_location)
        move_count += 1
    return move_count

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)