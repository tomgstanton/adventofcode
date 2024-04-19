dir = '2016/Day 19/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Memory():
    number_of_elves = int(inputline)
    circle = []

def MakeCircle():
    for number in range(Memory.number_of_elves):
        elf = {'elf':number+1}
        Memory.circle.append(elf)

def TakePresents():
    reduced_circle = []
    for index in range(len(Memory.circle)):
        if index % 2 == 0:
            reduced_circle.append(Memory.circle[index])
        if index % 2 == 0 and index == len(Memory.circle)-1:
            reduced_circle = [reduced_circle[-1]]+reduced_circle[:-1]
    Memory.circle = reduced_circle

def Calculate():
    MakeCircle()
    while len(Memory.circle) != 1:
        print(len(Memory.circle),Memory.circle[-1])
        TakePresents()
    return Memory.circle[0]['elf']

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)