import itertools

dir = '2015/Day 21/input.txt'
string = open(dir,'r')
inputlines = string.readlines()
dir = '2015/Day 21/input_shop.txt'
string = open(dir,'r')
inputlines_shop = string.readlines()

class BossStats():
    def __init__(self,):
        self.name = 'Boss'
        self.hitpoints = 0
        self.damage = 0
        self.armor = 0

class YouStats():
    def __init__(self,):
        self.name = 'You'
        self.hitpoints = 100
        self.damage = 0
        self.armor = 0

class MakeShop():
    def __init__(self,):
        self.stock = []
        self.options = []

def StockShop(inputlines):
    for line in inputlines:      
        splits = line.split()
        if len(splits) != 0 and splits[0][-1] == ':':
            item_type = splits[0][0:-1]
        if len(splits) != 0 and splits[0][-1] != ':':
            item = {
                'cost':int(splits[-3]),
                'damage':int(splits[-2]),
                'armor':int(splits[-1]),
                'name':''.join(splits[0:-3]),
                'type':item_type
            }
            shop.stock.append(item)

def SetBossStats(inputlines):
    for line in inputlines:
        splits = line.split()
        if splits[0] == 'Hit':
            boss.hitpoints = int(splits[-1])
        if splits[0] == 'Damage:':
            boss.damage = int(splits[-1])
        if splits[0] == 'Armor:':
            boss.armor = int(splits[-1])
    
def SetYouStats():
    you.hitpoints = 100
    you.damage = 0
    you.armor = 0

def Contest():
    combatants = [you,boss]
    while you.hitpoints >0 and boss.hitpoints >0:
        damage_dealt = max(1,(combatants[0].damage-combatants[1].armor))
        combatants[1].hitpoints -= damage_dealt
        combatants = combatants[::-1]
    # print(combatants[0].name,'defeated')
    # print(combatants[0].name,combatants[0].hitpoints)
    # print(combatants[1].name,combatants[1].hitpoints)
    return combatants[1]

def CheckSuitable(list):
    output = True
    weapon_count = 0
    armor_count = 0
    rings_count = 0
    for element in list:
        if element['type'] == 'Weapons':
            weapon_count += 1
        if element['type'] == 'Armor':
            armor_count += 1
        if element['type'] == 'Rings':
            rings_count += 1 
    if weapon_count != 1:
        output = False
    if armor_count > 1:
        output = False
    if rings_count > 2:
        output = False
    return output

def ProduceCombinations():
    shop.options.append([])
    for number in range(1,5):
        options = itertools.combinations(shop.stock,number)
        for option in options:
            if CheckSuitable(option) == True:
                shop.options.append(list(option))

def GearUp(option):
    output = 0
    for item in option:
        output += item['cost']
        you.damage += item['damage']
        you.armor += item['armor']
    return output

def Calculate(inputlines):
    lowest_spend = 1000
    ProduceCombinations()
    for option in shop.options:
        SetBossStats(inputlines)
        SetYouStats()
        spend = GearUp(option)
        winner = Contest()
        if winner.name == 'You' and spend < lowest_spend:
            print('Winner:',winner.name,', Total spend:',spend)
            for item in option:
                print(item['name'],item['cost'])
            lowest_spend = spend
    output = lowest_spend
    return output

if __name__ == '__main__':
    boss = BossStats()
    you = YouStats()
    shop = MakeShop()
    StockShop(inputlines_shop)
    answer = Calculate(inputlines)
    print('Answer is:',answer)