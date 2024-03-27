dir = '2016/Day 04/input.txt'
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
    encrypted_name = ''
    for split in splits:
        if split != splits[-1]:
            encrypted_name += split  
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

def CheckNames():
    output = 0
    for name in Encrypted.names:
        parsed_name = ParseName(name)
        checksum = CheckSum(parsed_name[0])
        if checksum == parsed_name[2]:
            output += int(parsed_name[1])
    return output

def Calculate(inputlines):
    ReadInput(inputlines)
    answer = CheckNames()
    return answer

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)