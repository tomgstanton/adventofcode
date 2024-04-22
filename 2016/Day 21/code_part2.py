dir = '2016/Day 21/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Memory():
    password = 'fbgdceah'
    instructions = inputlines[::-1]
 
def ApplyRule(splits):
    if splits[0] == 'swap' and splits[1] == 'position':
        index_1 = min(int(splits[2]),int(splits[5]))
        index_2 = max(int(splits[2]),int(splits[5]))
        Memory.password = Memory.password[:index_1]+Memory.password[index_2]+Memory.password[index_1+1:index_2]+Memory.password[index_1]+Memory.password[index_2+1:]
    if splits [0] == 'swap' and splits[1] == 'letter':
        Memory.password = Memory.password.replace(splits[2],'X')
        Memory.password = Memory.password.replace(splits[5],splits[2])
        Memory.password = Memory.password.replace('X',splits[5])
    if splits[0] == 'rotate' and splits[1] in ['left','right']:
        if splits[1] == 'right':
            index = len(Memory.password) - int(splits[2])
            Memory.password = Memory.password[-index:]+Memory.password[:-index]
        if splits[1] == 'left':
            index = len(Memory.password) - int(splits[2])
            Memory.password = Memory.password[index:]+Memory.password[:index]
    if splits[0] == 'rotate' and splits[1] == 'based':
        index = Memory.password.index(splits[6])
        if index %2 != 0:
            new_index = int((index+1)/2)
        if index % 2 == 0:
            new_index = int((len(Memory.password)+index)/2)+1
        if index == 0:
            new_index = 1
        Memory.password = Memory.password[new_index:]+Memory.password[:new_index]
    if splits[0] == 'reverse':
        index_1 = min(int(splits[2]),int(splits[4]))
        index_2 = max(int(splits[2]),int(splits[4]))
        Memory.password = Memory.password[:index_1]+Memory.password[index_1:index_2+1][::-1]+Memory.password[index_2+1:]
    if splits[0] == 'move':
        index_1 = int(splits[5])
        index_2 = int(splits[2])
        char_1 = Memory.password[index_1]
        Memory.password = Memory.password.replace(char_1,'')
        Memory.password = Memory.password[:index_2]+char_1+Memory.password[index_2:]

def Calculate():
    for instruction in Memory.instructions:
        splits = instruction.split()
        ApplyRule(splits)
    return Memory.password

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)