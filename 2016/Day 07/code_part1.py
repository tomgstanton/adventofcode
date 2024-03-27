dir = '2016/Day 07/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class IP():
    addresses = []
    split_addresses = []
    supports_TLS = []

def SplitAddresses():
    for address in IP.addresses:
        splits = address.split('[')
        split_entry = []
        for split in splits:
            if ']' not in split:
                split_entry.append(split)
            else:
                further_split = split.split(']')
                split_entry.append('['+further_split[0]+']')
                split_entry.append(further_split[1])
        IP.split_addresses.append(split_entry)

def Check(string):
    output = False
    for index in range(len(string)-3):
        if string[index] == string[index+3] and string[index+1] == string[index+2] and string[index] != string[index+1]:
            output = True
    return output

def SquareBracketsPass(address):
    output = True
    for split in address:
        if split[0] == '[' and Check(split) == True:
            output = False
    return output

def NonBracketsPass(address):
    output = False
    for split in address:
        if split[0] != '[' and Check(split) == True:
            output = True
    return output

def CheckTLSSupport():
    for address in IP.split_addresses:
        if SquareBracketsPass(address) == True and NonBracketsPass(address) == True:
            IP.supports_TLS.append(address)  

def Calculate(inputlines):
    for line in inputlines:
        if line[-1] == '\n':
            line = line[:-1]
        IP.addresses.append(line)
    SplitAddresses()
    CheckTLSSupport()
    return len(IP.supports_TLS)

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)