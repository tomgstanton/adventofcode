dir = '2016/Day 09/input.txt'
string = open(dir,'r')
inputline = string.readline()

def Calculate(inputline):
    output = ''
    char_index = 0
    while char_index < len(inputline):
        substring = inputline[char_index]
        new_index = char_index+1
        if inputline[char_index] == '(':
            splits = inputline[char_index+1:].split(')')
            marker = splits[0]
            further_splits = marker.split('x')
            subsequent_characters = inputline[char_index+2+len(marker):char_index+2+len(marker)+int(further_splits[0])]
            multiplier = int(further_splits[1])
            new_index = char_index+2+len(marker)+int(further_splits[0])
            substring = ''
            for number in range(multiplier):
                substring += subsequent_characters
        char_index = new_index
        output += substring
    return len(output)

if __name__ == '__main__':
    answer = Calculate(inputline)
    print('Answer is:',answer)