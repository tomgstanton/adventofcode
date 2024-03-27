dir = '2016/Day 07/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class IP():
    addresses = []
    split_addresses = []
    supports_SSL = []

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
    
def GetABAs(supernets):
    output = []
    for supernet in supernets:
        for index in range(len(supernet)-2):
            if supernet[index] == supernet[index+2]:
                output.append(supernet[index:index+3])
    return output

def CheckBABs(aba_orders,hypernets):
    output = False
    inverses = []
    for order in aba_orders:
        inverses.append(order[1:-1]+order[0:2])
    for hypernet in hypernets:
        for inverse in inverses:
            if inverse in hypernet:
                output = True
                break
    return output
        
def CheckSSL(address):
    output = False
    supernets = []
    hypernets = []
    for split in address:
        if split[0] == '[':
            hypernets.append(split)
        else:
            supernets.append(split)
    aba_orders = GetABAs(supernets)
    if CheckBABs(aba_orders,hypernets) == True:
        output = True
    return output
        
def CheckSSLSupport():
    for address in IP.split_addresses:
        if CheckSSL(address) == True:
            IP.supports_SSL.append(address)

def Calculate(inputlines):
    for line in inputlines:
        if line[-1] == '\n':
            line = line[:-1]
        IP.addresses.append(line)
    SplitAddresses()
    CheckSSLSupport()
    return len(IP.supports_SSL)

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)