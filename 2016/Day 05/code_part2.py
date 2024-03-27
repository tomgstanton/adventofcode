import hashlib

dir = '2016/Day 05/input.txt'
string = open(dir,'r')
inputline = string.readline()

def Calculate(inputline):
    output = '--------'
    fixed_positions = []
    index = 0
    while len(fixed_positions) != 8:
        position = 9
        teststring = inputline+str(index)
        md5string = hashlib.md5(teststring.encode('utf-8')).hexdigest()
        if index % 9999 == 0:
            print(output,md5string[5],md5string[6])
        if md5string[:5] == '00000' and md5string[5] in ['0','1','2','3','4','5','6','7']:            
            position = int(md5string[5])
            value = md5string[6]            
        if position in range(0,8) and position not in fixed_positions:
            fixed_positions.append(position)
            output = output[:position] + value + output[position+1:]
            print(output,md5string[5],md5string[6],'--DIGIT LOCKED--')
            
        index += 1
    return output

if __name__ == '__main__':
    answer = Calculate(inputline)
    print('Answer is:',answer)