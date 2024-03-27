dir = '2016/Day 06/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Tracker():
    dictionary = {}

def Track(string):
    for index in range(len(string)):
        pull = Tracker.dictionary.get(str(index))
        if pull == None:
            Tracker.dictionary[str(index)] = []
        Tracker.dictionary[str(index)].append(string[index])

def Calculate(inputlines):
    output = ''
    for line in inputlines:
        if line[-1] == '\n':
            line = line[:-1]
        Track(line)
    for entry in Tracker.dictionary:
        output += max(set(Tracker.dictionary[entry]), key=Tracker.dictionary[entry].count)
    return output

if __name__ == '__main__':
    answer = Calculate(inputlines)
    print('Answer is:',answer)