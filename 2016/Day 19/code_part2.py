import math

dir = '2016/Day 19/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Memory():
    number_of_elves = int(inputline)
    circle = []
    rejected_elves = []

def MakeCircle():
    for number in range(Memory.number_of_elves):
        elf = {'elf':number+1,'rejected':False}
        Memory.circle.append(elf)

def TakePresentsPro(): 
    back_reduced_circle = []
    front_reduced_circle = []
    circle = Memory.circle
    rejected_elves = 0
    mid_index = math.ceil(len(circle)/2)-1
    if len(circle) % 2 == 0:
           mid_index = int(len(circle)/2)
    for index in range(len(circle)):
        target_elf_index = index + mid_index        
        if index < mid_index and target_elf_index <= len(circle)-1:
            circle[target_elf_index]['rejected'] = True
            rejected_elves += 1
            back_reduced_circle.append(circle[index])
        else:
            if circle[index]['rejected'] == False:
                front_reduced_circle.append(circle[index])
        if (len(circle) - rejected_elves) % 2 == 0:
            mid_index +=1
    reduced_circle = front_reduced_circle + back_reduced_circle
    Memory.circle = reduced_circle


def TakePresents():    
    circle = Memory.circle
    for elf in circle:
        target_elf_index = circle.index(elf) - math.ceil((len(circle))/2)
        circle.remove(circle[target_elf_index])

def Calculate():
    MakeCircle()
    while len(Memory.circle) != 2:
        print(len(Memory.circle),Memory.circle[-1])
        TakePresentsPro()
    return Memory.circle[0]['elf']

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)