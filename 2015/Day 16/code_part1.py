dir = '2015/Day 16/input.txt'
string = open(dir,'r')
inputlines = string.readlines()
dir = '2015/Day 16/further_input.txt'
string = open(dir,'r')
furtherinputlines = string.readlines()

class Sues():
    def __init__(self,):
        self.viablelist = inputlines

def MakeDictionary(lines):
    dict = {}
    for line in inputlines:
        line = line.replace('\n','')
        line = line.replace(':','')
        line = line.replace(',','')
        elements = line.split(' ')
        dict[elements[1]] = {elements[2]:elements[3],elements[4]:elements[5],elements[6]:elements[7]}
    return dict    

def CheckQuality(quality):
    quality = quality.replace('\n','')
    quality = quality.replace(':','')
    elements = quality.split(' ')
    newviabledict = {}
    for x in sues.viablelist:
        value = sues.viablelist[x].get(elements[0])
        if value == None:
            newviabledict[x] = sues.viablelist[x]
        if value == elements[1]:
            newviabledict[x] = sues.viablelist[x]
    sues.viablelist = newviabledict

def Calculate(furtherinputlines):
    for x in furtherinputlines:
        CheckQuality(x)
    return sues.viablelist

sues = Sues()
sues.viablelist = MakeDictionary(sues.viablelist)
answer = Calculate(furtherinputlines)
print('Answer is:',answer)