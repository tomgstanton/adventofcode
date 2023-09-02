dir = '2015/Day 10/input.txt'
string = open(dir,'r')
inputline = string.read()

def ElfSay(line):
    output = ''
    count = 1
    for index in range(len(line)):
        if index !=0 and line[index-1] == line[index]:
            count += 1
        if index !=0 and line[index-1] != line[index]:
            output += str(count)+line[index-1]
            count = 1
    output += str(count)+line[-1]        
    return output

def Calculate(line):
    for x in range(50):
        line = ElfSay(line)
    return len(line)

answer = Calculate(inputline)
print('Answer is:',answer)