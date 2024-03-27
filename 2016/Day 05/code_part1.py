import hashlib

dir = '2016/Day 05/input.txt'
string = open(dir,'r')
inputline = string.readline()

def Calculate(inputline):
    output = ''
    index = 0
    while len(output) != 8:
        teststring = inputline+str(index)
        md5string = hashlib.md5(teststring.encode('utf-8')).hexdigest()
        if md5string[:5] == '00000':
            output += md5string[5]
        index += 1
    return output

if __name__ == '__main__':
    answer = Calculate(inputline)
    print('Answer is:',answer)