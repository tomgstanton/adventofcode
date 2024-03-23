def GenerateNumbers(startingnumber):
    output = [startingnumber]
    row = 1
    column = 1 
    while len(output) < 999999999:
        value = (output[-1] * 252533) % 33554393
        row -= 1
        column += 1
        if row == 0:
            row = column
            column = 1
        output.append(value)
        if row == 3010 and column == 3019:
            return output[-1]

def Calculate():
    answer = GenerateNumbers(20151125)
    return answer

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)