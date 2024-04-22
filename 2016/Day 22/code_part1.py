dir = '2016/Day 22/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Memory():
    data = inputlines
    nodes = []
    nonempty_nodes = []
    viable_pairs = []

def ReadData():
    for line in Memory.data:
        if line[-1] == '\n':
            line = line[:-1]
        splits = line.split()
        if '-' in splits[0]:
            splits[0] = splits[0].split('-')
        if line[0] == '/':
            entry = {'x-axis':int(splits[0][1][1:]),'y-axis':int(splits[0][2][1:]),'used':int(splits[2][:-1]),'avail':int(splits[3][:-1])}
            Memory.nodes.append(entry)
            if entry['used'] != 0:
                Memory.nonempty_nodes.append(entry)

def Calculate():
    ReadData()
    for node_A in Memory.nonempty_nodes:
        for node_B in Memory.nodes:
            if node_A != node_B and node_A['used'] <= node_B['avail']:
                Memory.viable_pairs.append([node_A,node_B])
    return len(Memory.viable_pairs)

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)