dir = '2015/Day 19/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Replacements():
    def __init__(self,):
        self.replacements = {}
        self.molecules = {}
        self.target = ''
        self.answer = 0

def LoadRule(string):
    components = string.split()
    if len(components) == 3:
        rule_input = rules.replacements.get(components[2])
        if rule_input == None:
            rules.replacements[components[2]] = [components[0]]
        else:
            rule_output = rules.replacements[components[2]]
            rule_output.append(components[0])
            rules.replacements[components[2]] = rule_output

def MakeReplacementDictionary(lines):
    for x in lines:
        x = x.replace('\n','')
        LoadRule(x)
    rules.molecules[0] = [lines[-1]]

def ApplyRules(molecule):
    output = []
    for i in range(len(molecule)):
        stop = 0
        if i != 8 and stop == 0:
            dectuple = molecule[i-9:i+1] 
            replacements = rules.replacements.get(dectuple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-9]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 7 and stop == 0:
            nontuple = molecule[i-8:i+1] 
            replacements = rules.replacements.get(nontuple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-8]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 6 and stop == 0:
            octuple = molecule[i-7:i+1] 
            replacements = rules.replacements.get(octuple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-7]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 5 and stop == 0:
            heptuple = molecule[i-6:i+1] 
            replacements = rules.replacements.get(heptuple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-6]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 4 and stop == 0:
            sextuple = molecule[i-5:i+1] 
            replacements = rules.replacements.get(sextuple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-5]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 3 and stop == 0:
            quintuple = molecule[i-4:i+1] 
            replacements = rules.replacements.get(quintuple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-4]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 2 and stop == 0:
            quadruple = molecule[i-3:i+1] 
            replacements = rules.replacements.get(quadruple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-3]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 1 and stop == 0:
            triple = molecule[i-2:i+1] 
            replacements = rules.replacements.get(triple)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-2]+replacement+molecule[i+1:]
                    output.append(new_molecule)
                stop = 1
        if i != 0 and stop == 0:
            double = molecule[i-1:i+1] 
            replacements = rules.replacements.get(double)
            if replacements != None:
                for replacement in replacements:
                    new_molecule = molecule[0:i-1]+replacement+molecule[i+1:]
                    output.append(new_molecule)
    output = list(set(output))
    return output

def Calculate (lines):
    MakeReplacementDictionary(lines)
    step = 0
    while True:
        molecules = rules.molecules.get(step)
        molecules = list(set(molecules))
        molecules.sort(key=lambda s: len(s))
        molecules = molecules[0:100]
        if 'e' in molecules:
            rules.answer = step
            break  
        step += 1
        rules.molecules[step] = []
        for molecule in molecules:
            new_molecules = ApplyRules(molecule)
            rules.molecules[step] = rules.molecules[step] + new_molecules
        rules.molecules = {step:rules.molecules[step]}

rules = Replacements()
Calculate(inputlines)
print('Answer is:',rules.answer)
