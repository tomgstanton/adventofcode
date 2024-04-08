import math

dir = '2016/Day 09/input.txt'
string = open(dir,'r')
inputline = string.readline()

def GetScopeMultiplier(multipliers_dict):
    output = []
    for entry in multipliers_dict:
        markers = multipliers_dict[entry]
        for marker in markers:
            output.append(marker[1])
    output = math.prod(output)
    return output

def Calculate(inputline):
    output_length = 0
    char_index = 0
    multipliers_dict = {}
    while char_index < len(inputline):
        added_length = 0
        dict_entry = multipliers_dict.get(char_index)
        if dict_entry != None:
            scope_multiplier = GetScopeMultiplier(multipliers_dict)
            added_length += dict_entry[-1][0]*scope_multiplier
            multipliers_dict.pop(char_index)
        if inputline[char_index] == '(':
            splits = inputline[char_index+1:].split(')')
            marker = splits[0]
            further_splits = marker.split('x')
            resuming_index = char_index+1+len(marker)+int(further_splits[0])
            dict_entry = multipliers_dict.get(resuming_index)
            if dict_entry == None:
                multipliers_dict[resuming_index] = []
            multipliers_dict[resuming_index].append([int(further_splits[0]),int(further_splits[1])])
        char_index += 1
        output_length += added_length
    return output_length

if __name__ == '__main__':
    answer = Calculate(inputline)
    print('Answer is:',answer)