dir = '2016/Day 16/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Memory():
    line = inputline
    enough_data = line
    data = ''

def DragonCurve():
    a = Memory.enough_data
    b = a[::-1]
    inverse_b = ''
    for char in b:
        if char == '0':
            inverse_b += '1'
        if char == '1':
            inverse_b += '0'
    Memory.enough_data = a+'0'+inverse_b

def CurtailData(number):
    Memory.data = Memory.enough_data[:number]
    
def FillDisk(number):
    while len(Memory.enough_data) < number:
        DragonCurve()
    CurtailData(number)

def Round(string):
    output = ''
    for index in range(len(string)-1):
        if index % 2 == 0 and string[index] == string[index+1]:
            output += '1'
        if index % 2 == 0 and string[index] != string[index+1]:
            output += '0'
    return output

def CheckSum():
    output = Memory.data
    while len(output) % 2 == 0:
        output = Round(output)
    return output

def Calculate():
    FillDisk(272)
    return CheckSum()

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)