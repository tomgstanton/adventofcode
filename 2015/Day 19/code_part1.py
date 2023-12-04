dir = '2015/Day 19/input.txt'
string = open(dir,'r')
inputlines = string.readlines()

class Replacements():
    def __init__(self,):
        self.replacements = {}
        self.molecule = ''

def LoadRule(string):
    components = string.split()
    if len(components) == 3:
        rule_input = rules.replacements.get(components[0])
        if rule_input == None:
            rules.replacements[components[0]] = [components[2]]
        else:
            rule_output = rules.replacements[components[0]]
            rule_output.append(components[2])
            rules.replacements[components[0]] = rule_output

def MakeReplacementDictionary(lines):
    for x in lines:
        x = x.replace('\n','')
        LoadRule(x)

def ApplyRules():
    output = []
    for i in range(len(rules.molecule)):
        single = rules.molecule[i] 
        replacements = rules.replacements.get(single)
        if replacements != None:
            for replacement in replacements:
                molecule = rules.molecule[0:i]+replacement+rules.molecule[i+1:]
                output.append(molecule)
        if i != 0:
            double = rules.molecule[i-1:i+1] 
            replacements = rules.replacements.get(double)
            if replacements != None:
                for replacement in replacements:
                    molecule = rules.molecule[0:i-1]+replacement+rules.molecule[i+1:]
                    output.append(molecule)
    output = set(output)
    return output

def Calculate (lines):
    MakeReplacementDictionary(lines)
    rules.molecule = lines[-1]
    output = ApplyRules() 
    return len(output)

rules = Replacements()
answer = Calculate(inputlines)
print('Answer is:',answer)
