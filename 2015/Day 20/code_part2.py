dir = '2015/Day 20/input.txt'
string = open(dir,'r')
inputline = string.readline()

class Target():
    def __init__(self,):
        self.value = 0

def GetFactors(n):  
    output = set(factor for i in range(1, int(n**0.5) + 1) if n % i == 0 for factor in (i, n//i))
    return output

def GetDiscount(factors,limit):
    output = 0
    for factor in factors:
        if factor * 50 < limit:
            output += factor
    return output

def Calculate (line):
    output = 'working'
    target.value = int(line)
    for number in range(1000000):
        factors = GetFactors(number)
        discount = GetDiscount(factors,number)        
        value = (sum(factors)-discount)*11
        if value >= target.value:
            output = number
            break
    return output

target = Target()
answer = Calculate(inputline)
print('Answer is:',answer)
