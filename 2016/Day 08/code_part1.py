dir = '2016/Day 08/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Display():
    instructions = []
    pixels = []

def GetInstructions(inputlines):
    for line in inputlines:
        if line[-1] == '\n':
            line = line[:-1]
        Display.instructions.append(line)

def MakePixels(width,height):
    for row in range(height):
        row = []
        for column in range(width):
            row.append(0)
        Display.pixels.append(row)

def ApplyRect(width,height):
    for row_index in range(len(Display.pixels)):
        for column_index in range(len(Display.pixels[row_index])):
            if column_index < width and row_index < height:
                Display.pixels[row_index][column_index] = 1

def ApplyRotateRow(index,adjust):
    temp_row = Display.pixels[index]
    adjusted_row = temp_row[-adjust:]+temp_row[:-adjust]
    Display.pixels[index] = adjusted_row

def ApplyRotateColumn(index,adjust):
    temp_column = []
    for row in Display.pixels:
        temp_column.append(row[index])
    adjusted_column = temp_column[-adjust:]+temp_column[:-adjust]
    for row_index in range(len(Display.pixels)):
        Display.pixels[row_index][index] = adjusted_column[row_index]        

def ApplyInstructions():
    for instruction in Display.instructions:
        splits = instruction.split()
        if splits[0] == 'rect':
            dimensions = splits[1].split('x')
            width = int(dimensions[0])
            height = int(dimensions[1])
            ApplyRect(width,height)
        if splits[1] == 'row':
            index = int(splits[2][2:])
            adjust = int(splits[4])
            ApplyRotateRow(index,adjust)
        if splits[1] == 'column':
            index = int(splits[2][2:])
            adjust = int(splits[4])
            ApplyRotateColumn(index,adjust)

def CountLitPixels():
    output = 0
    for row in Display.pixels:
        output += sum(row)
    return output

def Calculate(inputlines):
    GetInstructions(inputlines)
    MakePixels(50,6)
    ApplyInstructions()
    answer = CountLitPixels()
    return answer

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)