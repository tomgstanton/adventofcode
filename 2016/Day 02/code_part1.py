dir = '2016/Day 02/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Keypad():
    location = 5

def MoveUp():
    columns = [[7,4,1],[8,5,2],[9,6,3]]
    for column in columns:
        if Keypad.location in column:
            new_location_index = min(2,column.index(Keypad.location)+1)
            Keypad.location = column[new_location_index]

def MoveDown():
    columns = [[7,4,1],[8,5,2],[9,6,3]]
    for column in columns:
        if Keypad.location in column:
            new_location_index = max(0,column.index(Keypad.location)-1)
            Keypad.location = column[new_location_index]

def MoveRight():
    rows = [[1,2,3],[4,5,6],[7,8,9]]
    for row in rows:
        if Keypad.location in row:
            new_location_index = min(2,row.index(Keypad.location)+1)
            Keypad.location = row[new_location_index]

def MoveLeft():
    rows = [[1,2,3],[4,5,6],[7,8,9]]
    for row in rows:
        if Keypad.location in row:
            new_location_index = max(0,row.index(Keypad.location)-1)
            Keypad.location = row[new_location_index]

def Track(line):
    for x in line:
        if x == 'U':
            MoveUp()
        if x == 'D':
            MoveDown()
        if x == 'R':
            MoveRight()
        if x == 'L':
            MoveLeft()

def Calculate(inputlines):
    answer = ''
    for line in inputlines:
        if line[-1] == '\n':
            line = line[:-1]
        Track(line)
        answer += str(Keypad.location)
    return answer

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)