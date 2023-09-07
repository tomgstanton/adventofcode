import re

dir = '2015/Day 14/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

def ExtractNumbers(x):
    extracted = re.findall(r'[-+]?\d+',str(x))
    return [int(s) for s in extracted]

def StartRace(numbers,time_limit):
    template = numbers[:]
    distance = 0
    distance_array = []
    second = 1
    while second != time_limit+1: 
        if template[1] == 0 and template[3] != 0:
            distance += template[2]
            distance_array.append(distance)
            template[3] -= 1            
        if template[1] != 0:
            distance += template[0]
            distance_array.append(distance)
            template[1] -= 1
        if template[1] == 0 and template[1] == template[3]:
            template = numbers[:]
        second += 1
    return distance_array

def ScoreRunners(array):
    scores = []
    for runner in array:
        scores.append(0)
    for index in range(len(array[0])):
        current_distances = []
        for runner_index in range(len(array)):
            current_distances.append(array[runner_index][index])
        for distance_index in range(len(current_distances)):
            if current_distances[distance_index] == max(current_distances):
                scores[distance_index] += 1
    return max(scores)

def Calculate(lines,time_limit):
    array = []
    for line in lines:
        numbers = ExtractNumbers(line)
        numbers.insert(2,0)
        distance = StartRace(numbers,time_limit)
        array.append(distance)
    output = ScoreRunners(array)
    return output

answer = Calculate(inputlines,2503)
print('Answer is:',answer)