import itertools

dir = '2015/Day 17/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Results():
    def __init__(self,):
        self.groups = []
        self.instances = {}

def GetPowerset(group):
    group_set = set(group)
    length = len(group_set)
    masks = [1 << i for i in range(length)]
    for i in range(1 << length):
        yield [ss for mask, ss in zip(masks, group_set) if i & mask]

def GetDuplicates():
    output = []
    for entry in combinations.instances:
        if combinations.instances[entry] != 1:
            for number in range(combinations.instances[entry]-1):
                output.append(entry)
    return output

def Calculate(lines):
    boxes = []
    for x in lines:
        x = x.replace('\n','')
        boxes.append(int(x))
    for x in boxes:
        value = combinations.instances.get(x)
        if value is None:
            combinations.instances[x] = boxes.count(x)
    powerset_list = list(GetPowerset(boxes))
    duplicates_powerset_list = list(GetPowerset(GetDuplicates()))
    temporary_groups = []
    for r in itertools.product(powerset_list, duplicates_powerset_list): temporary_groups.append(r[0]+r[1])
    for x in temporary_groups:
        if sum(x) == 150:
            combinations.groups.append(x)
    return len(combinations.groups)

combinations = Results()
answer = Calculate(inputlines)
print('Answer is:',answer)