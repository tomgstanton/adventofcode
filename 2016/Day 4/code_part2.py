dir = '2016/Day 4/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Encrypted():
    names = []

def ReadInput(inputlines):
    for line in inputlines:
        if line[-1] == '\n':
            line = line[:-1]
        Encrypted.names.append(line)

def ParseName(name):
    splits = name.split('-')
    span = len(splits[-1])+1
    encrypted_name = name[:-span]
    further_splits = splits[-1].split('[')
    sector_id = further_splits[0]
    checksum = further_splits[1][:-1]
    parsed_name = [encrypted_name,sector_id,checksum]
    return parsed_name

def CheckSum(name):
    counts = []
    for x in name:
        count = name.count(x)
        entry = {'letter':x,'count':count}
        if entry not in counts:
            counts.append(entry)
    counts = sorted(counts,key=lambda x: x['letter'])[::-1]
    counts = sorted(counts,key=lambda x: x['count'])[::-1]
    output = ''
    for count in counts:
        if len(output) == 5:
            return output
        output += count['letter']

def GetMap(number):
    map = {'-':' '}
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    adjust = number % len(alphabet)
    changed_alphabet = alphabet[adjust:]+alphabet[:adjust]
    for letter in alphabet:
        map[letter] = changed_alphabet[alphabet.index(letter)]
    return map

def EasterCheck(name):
    contraband = ['egg','dye','rabbit','jellybean','chocolate','bunny','scavenger','grass','candy','flower','basket']
    for item in contraband:
        if item in name:
            return True
    return False

def CheckNames():
    output = []
    for name in Encrypted.names:
        parsed_name = ParseName(name)
        letter_map = GetMap(int(parsed_name[1]))
        changed_name = ''
        for letter in parsed_name[0]:
            new_letter = letter_map.get(letter)
            changed_name += new_letter
        if EasterCheck(changed_name) == False:
            output.append([changed_name,parsed_name[1]])
    return output

def Calculate(inputlines):
    ReadInput(inputlines)
    answer = CheckNames()
    return answer

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)


    