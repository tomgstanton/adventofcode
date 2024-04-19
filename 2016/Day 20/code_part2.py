dir = '2016/Day 20/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Memory:
    ip_addresses = inputlines
    unblocked_ranges = [[0,4294967295]]

def Calculate():
    for address in Memory.ip_addresses:
        if address[-1] == '\n':
            address = address[:-1]
        splits = address.split('-')
        splits = [int(splits[0]),int(splits[1])]
        old_entries = []
        new_entries = []
        for unblocked_range in Memory.unblocked_ranges:
            if splits[0] >= unblocked_range[0] and splits[0] <= unblocked_range[1]:
                if unblocked_range not in old_entries:
                    old_entries.append(unblocked_range)
                if splits[0]-1 >= unblocked_range[0]:
                    new_entries.append([unblocked_range[0],splits[0]-1])
            if splits[1] >= unblocked_range[0] and splits[0] <= unblocked_range[1]:
                if unblocked_range not in old_entries:
                    old_entries.append(unblocked_range)
                if unblocked_range[1] >= splits[1]+1:
                    new_entries.append([splits[1]+1,unblocked_range[1]])
        for old_entry in old_entries:
            Memory.unblocked_ranges.remove(old_entry)
        for new_entry in new_entries:
            Memory.unblocked_ranges.append(new_entry)
        Memory.unblocked_ranges.sort()
    output = 0
    for unblocked_range in Memory.unblocked_ranges:
        output += unblocked_range[1] - unblocked_range[0] + 1
    return output

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)