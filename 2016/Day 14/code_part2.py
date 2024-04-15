import hashlib

dir = '2016/Day 14/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Memory():
    salt = inputline
    pad_keys = []
    character = ''
    hashed_strings = {}

def FindTriplet(hash):
    output = False
    for index in range(len(hash)-2):
        if hash[index] == hash[index+1] and hash[index] == hash[index+2]:
            target_three = hash[index:index+3]
            Memory.character = hash[index]
            if hash.count(target_three) == 1:
                output = True
                break
    return output

def FindQuintet(index):
    output = False
    for number in range(index+1,index+1001):
        new_string = Memory.salt+str(number)
        new_hash = Memory.hashed_strings.get(new_string)
        if new_hash == None:
            new_hash = StretchHash(new_string)
            Memory.hashed_strings[new_string] = new_hash
        target_five = 5*Memory.character
        if new_hash.count(target_five) == 1:
            output = True
            break
    return output

def CheckKey(hash,index):
    output = False
    if FindTriplet(hash) is True and FindQuintet(index) is True:
        output = True
    return output

def StretchHash(string):
    number = 1
    while number < 2018:
        string = hashlib.md5(string.encode('utf-8')).hexdigest()
        number += 1
    return string

def Calculate():
    index = 0
    while len(Memory.pad_keys) != 64:
        string = Memory.salt+str(index)
        hash = Memory.hashed_strings.get(string)
        if hash == None:
            hash = StretchHash(string)
            Memory.hashed_strings[string] = hash
        if CheckKey(hash,index) is True:            
            Memory.pad_keys.append(string)
        index += 1
        if Memory.pad_keys != []:
            print(Memory.pad_keys[-1])
    return index-1

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)