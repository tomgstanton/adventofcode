dir = '2015/Day 22/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class BossStats():
    def __init__(self,):
        self.hitpoints = 0
        self.damage = 0
        self.armor = 0

class YouStats():
    def __init__(self,):
        self.hitpoints = 50
        self.mana = 500
        self.damage = 0
        self.armor = 0 

class SpellStats():
    def __init__(self,):
        self.repertoire = [
            {'name':'Magic Missile',
             'cost':53,
             'damage':4,
             'healing':0,
             'lasting':0},
            {'name':'Drain',
             'cost':73,
             'damage':2,
             'healing':2,
             'lasting':0},
            {'name':'Shield',
             'cost':113,
             'damage':0,
             'healing':0,             
             'lasting':6,
             'armor':7,
             'starting_damage':0,
             'new_mana':0},
            {'name':'Poison',
             'cost':173,
             'damage':0,
             'healing':0,
             'lasting':6,
             'starting_damage':3,
             'new_mana':0},
            {'name':'Recharge',
             'cost':229,
             'damage':0,
             'healing':0,
             'lasting':5,
             'starting_damage':0,
             'new_mana':101},
        ]
        self.options = []
        self.current_options = []
        self.option_to_check = []
        self.lasting = []
        self.trashorders = []
        self.surviving_options = []

def SetBossStats(inputlines):
    for line in inputlines:
        splits = line.split()
        if splits[0] == 'Hit':
            boss.hitpoints = int(splits[-1])
        if splits[0] == 'Damage:':
            boss.damage = int(splits[-1])

def SetYouStats():
    you.hitpoints = 50
    you.mana = 500
    you.damage = 0
    you.armor = 0   

def GetSpellOptions(number):
    spell.options = sorted(spell.options, key=lambda d: d['cost'])
    spell.current_options = []
    for option in spell.options:
        if option['cost'] == number:
            spell.current_options.append(option)
        if option['cost'] > number:
            return

def ExpandOptions():
    if spell.options == []:
        for item in spell.repertoire:
            spell.options.append({'cost':item['cost'],'spells':[item]}) 
    for option in spell.surviving_options:
        for item in spell.repertoire:
            spell.options.append({'cost':option['cost']+item['cost'],'spells':option['spells']+[item]})

def ResetYouStats():
    you.damage = 0

def StartOfTurnEffects():
    adjusted_lasting_spells = []
    for lasting_spell in spell.lasting:        
        boss.hitpoints -= lasting_spell[0]['starting_damage']
        you.mana += lasting_spell[0]['new_mana']
        lasting_spell[1] -= 1
        if lasting_spell[1] == 0 and lasting_spell[0]['name'] == spell.repertoire[2]['name']:
            you.armor = 0
        if lasting_spell[1] != 0:
            adjusted_lasting_spells.append(lasting_spell)
    spell.lasting = adjusted_lasting_spells

def SpellCastable():
    output = True
    if you.mana < spell.option_to_check['spells'][0]['cost']:
        output = False
    for lasting_spell in spell.lasting:
        if lasting_spell[0]['name'] == spell.option_to_check['spells'][0]['name']:
            output = False
    return output

def CastSpell():
    you.mana -= spell.option_to_check['spells'][0]['cost']
    boss.hitpoints -= spell.option_to_check['spells'][0]['damage']
    you.hitpoints += spell.option_to_check['spells'][0]['healing']
    if spell.option_to_check['spells'][0]['name'] == 'Shield':
        you.armor = spell.option_to_check['spells'][0]['armor']
    if spell.option_to_check['spells'][0]['lasting'] != 0:
        spell.lasting.append([spell.option_to_check['spells'][0],spell.option_to_check['spells'][0]['lasting']])
    spell.option_to_check['spells'] = spell.option_to_check['spells'][1:]  

def Contest():
    combatants = [you,boss]
    spell.lasting = []
    tracker = []
    while you.hitpoints > 0 and boss.hitpoints > 0:
        if combatants[0] == you:
            you.hitpoints -= 1
        if you.hitpoints <= 0:
            spell.trashorders.append(tracker)
            break
        ResetYouStats()
        StartOfTurnEffects()
        if boss.hitpoints <= 0:
            break
        if spell.option_to_check['spells'] == [] and tracker != []:
            break 
        if combatants[0] == you and SpellCastable() == False:
            tracker.append(spell.option_to_check['spells'][0])
            spell.trashorders.append(tracker)
            break
        if combatants[0] == you and SpellCastable() == True:
            tracker.append(spell.option_to_check['spells'][0])
            CastSpell()    
        if boss.hitpoints <= 0:
            break
        if combatants[0] == boss:
            damage_dealt = max(1,(combatants[0].damage-combatants[1].armor))
            combatants[1].hitpoints -= damage_dealt
        combatants = combatants[::-1]
    if you.hitpoints <= 0:
        spell.trashorders.append(tracker)

def CheckTrash(listofspells):
    output = False
    for trashorder in spell.trashorders:                
        span = len(trashorder)        
        if listofspells['spells'][0:span] == trashorder:
            output = True
    return output

def CleanOptions():      
    for candidate_option in spell.current_options:  
        spell.options.remove(candidate_option) 
    spell.trashorders = []

def Calculate(inputlines):
    SetBossStats(inputlines)
    spend_number = 0
    while True:
        GetSpellOptions(spend_number)
        spell.surviving_options = []
        for checking_order in spell.current_options:
            SetBossStats(inputlines)
            SetYouStats()
            spell.option_to_check = checking_order.copy()
            if CheckTrash(spell.option_to_check) == False:
                Contest()
                if boss.hitpoints <= 0 and you.hitpoints > 0:
                    return spend_number
            if CheckTrash(checking_order) == False:
                spell.surviving_options.append(checking_order)
        CleanOptions()
        ExpandOptions()
        print(spend_number)
        spend_number += 1

if __name__ == '__main__':
    boss = BossStats()
    you = YouStats()
    spell = SpellStats()
    answer = Calculate(inputlines)
    print('Answer is:',answer)
