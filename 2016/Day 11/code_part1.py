from copy import deepcopy
import itertools

class Moves():
    archive = []
    previous = []
    next = []
    surviving = []
    number = 0

class Building():
    floors = [{'microchip':['SM','PM'],'generator':['SG','PG']},
              {'microchip':['RM','TM'],'generator':['RG','TG','QG']},
              {'microchip':['QM'],'generator':[]},
              {'microchip':[],'generator':[]}]
    elevator = 0

def GetMovingCandidates():
    moving_candidates = []
    group = Building.floors[Building.elevator]['microchip']+Building.floors[Building.elevator]['generator']
    for item in group:
        moving_candidates.append([item])
    combinations = itertools.combinations(group,2)
    for item in combinations:
        moving_candidates.append(list(item))
    return moving_candidates

def ResetBuilding(arrangement):
    Building.floors = deepcopy(arrangement[0])
    Building.elevator = deepcopy(arrangement[1])

def MoveUp(candidate):
    for item in candidate:
        if item in Building.floors[Building.elevator]['microchip']:
            Building.floors[Building.elevator]['microchip'].remove(item)
            Building.floors[Building.elevator+1]['microchip'].append(item)
        if item in Building.floors[Building.elevator]['generator']:
            Building.floors[Building.elevator]['generator'].remove(item)        
            Building.floors[Building.elevator+1]['generator'].append(item)
    Building.elevator += 1
    if [deepcopy(Building.floors),deepcopy(Building.elevator)] not in Moves.next:
        Moves.next.append([deepcopy(Building.floors),deepcopy(Building.elevator),Score(deepcopy(Building.floors))])

def MoveDown(candidate):
    for item in candidate:
        if item in Building.floors[Building.elevator]['microchip']:
            Building.floors[Building.elevator]['microchip'].remove(item)
            Building.floors[Building.elevator-1]['microchip'].append(item)
        if item in Building.floors[Building.elevator]['generator']:
            Building.floors[Building.elevator]['generator'].remove(item)        
            Building.floors[Building.elevator-1]['generator'].append(item)
    Building.elevator -= 1
    if [deepcopy(Building.floors),deepcopy(Building.elevator)] not in Moves.next:
        Moves.next.append([deepcopy(Building.floors),deepcopy(Building.elevator),Score(deepcopy(Building.floors))])    

def FriedChips(arrangement):
    survive = False
    for floor in arrangement[0]:
        needed_generators = []
        for microchip in floor['microchip']:
            needed_generators.append(microchip[0]+'G')
        for generator in needed_generators:
            if generator not in floor['generator'] and len(floor['generator']) != 0:
                survive = True
    return survive
                
def CheckForFriedChips():
    for arrangement in Moves.next:
        if FriedChips(arrangement) == False and arrangement not in Moves.archive:
            Moves.surviving.append(arrangement)
            Moves.archive.append(arrangement)    
    Moves.next = []
    
def CheckAllOnFloor4():
    output = False
    number_of_microchips_and_generators = 0
    for floor in Building.floors:
        number_of_microchips_and_generators += len(floor['microchip'])
        number_of_microchips_and_generators += len(floor['generator'])
    for arrangement in Moves.previous:
        if len(arrangement[0][3]['microchip'])+len(arrangement[0][3]['generator']) == number_of_microchips_and_generators:
            output = True
    return output

def Prune():
    Moves.surviving = sorted(Moves.surviving, key=lambda x: x[2])[::-1]
    output = []
    checked_scores = []
    for arrangement in Moves.surviving:
        if arrangement[2] not in checked_scores:
            output.append(arrangement)
            checked_scores.append(arrangement[2])
    return output

def Progress():
    if len(Moves.surviving) > 20:
        Moves.surviving = Prune()
    Moves.previous = deepcopy(Moves.surviving)    
    Moves.surviving = []
    Moves.number += 1

def Score(floors):
    value = 0
    magnitude = 0
    for floor in floors:
        value += (len(floor['microchip']) * (10**magnitude)) * (len(floor['generator'])) * (10**magnitude)
        magnitude += 1
    return value

def Calculate():
    Moves.previous.append([Building.floors,Building.elevator,Score(Building.floors)])
    while CheckAllOnFloor4() is False:
        for arrangement in Moves.previous:
            ResetBuilding(arrangement)
            candidates = GetMovingCandidates()
            for candidate in candidates:
                if Building.elevator != 3 and len(candidate) == 2:
                    MoveUp(candidate)
                    ResetBuilding(arrangement)
                if Building.elevator != 0 and len(candidate) == 1:                
                    MoveDown(candidate)
                    ResetBuilding(arrangement) 
            CheckForFriedChips()
        print(len(Moves.previous),Moves.number)
        Progress()
    return Moves.number

if __name__ == '__main__':
    answer = Calculate()
    print('Answer is:',answer)