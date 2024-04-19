dir = '2016/Day 18/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Memory():
    rows = [inputline]

def MakeNextRow():
    print(Memory.rows[-1])
    next_row = ''
    previous_row = Memory.rows[-1]
    for index in range(len(previous_row)):
        left = previous_row[index-1]
        if index == 0:
            left = '.'
        centre = previous_row[index]
        if index != len(previous_row)-1:
            right = previous_row[index+1]
        if index == len(previous_row)-1:
            right = '.'
        former_tiles = left+centre+right
        tile = '.'
        if former_tiles in ['^^.','.^^','^..','..^']:
            tile = '^'
        next_row += tile
    Memory.rows.append(next_row)

def CountSafeTiles():
    output = 0
    for row in Memory.rows:
        output += row.count('.')
    return output

def Calculate():
    while len(Memory.rows) != 40:
        MakeNextRow()
    return CountSafeTiles()

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)