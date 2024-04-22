dir = '2016/Day 21/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Memory():
    password = 'abcdefgh'
    instructions = inputlines

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
            index = int(splits[2])
            Memory.password = Memory.password[-index:]+Memory.password[:-index]
        if splits[1] == 'left':
            index = int(splits[2])
            Memory.password = Memory.password[index:]+Memory.password[:index]
    if splits[0] == 'rotate' and splits[1] == 'based':
        index = Memory.password.index(splits[6])
        times = index +1
        if index >= 4:
            times += 1
        for number in range(times):
            Memory.password = Memory.password[-1:]+Memory.password[:-1]        
    if splits[0] == 'reverse':
        index_1 = min(int(splits[2]),int(splits[4]))
        index_2 = max(int(splits[2]),int(splits[4]))
        Memory.password = Memory.password[:index_1]+Memory.password[index_1:index_2+1][::-1]+Memory.password[index_2+1:]
    if splits[0] == 'move':
        index_1 = int(splits[2])
        index_2 = int(splits[5])
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