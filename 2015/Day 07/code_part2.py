import code_part1

dir = '2015/Day 07/input part2.txt'
string = open(dir,'r')
inputlines = string.readlines()

Values = code_part1.ValuesDict()
code_part1.Calculate(inputlines)

results = ['a']
for result in results:
    print('Answer is:',result,'=',code_part1.Values.values[result])