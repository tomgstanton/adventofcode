import code_part1

dir = '2015/Day 11/input.txt'
string = open(dir,'r')
inputline = string.read()

prioranswer = code_part1.Calculate(inputline)
answer = code_part1.Calculate(prioranswer)
print('Answer is:',answer)