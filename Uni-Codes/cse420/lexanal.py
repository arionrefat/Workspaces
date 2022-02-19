syntaxWords = ['if', 'else', 'for']
varini = ['int', 'double', 'float']
operators = ['+', '-', '=']
logicalops = ['>']
otherstuffs = [',', '(', ')', ';', '{', '}']

keywords = list()
identifiers = list()
mathoperator = list()
logicaloperator = list()
numericalvalues = list()
others = list()

with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()

        for i in otherstuffs:
            line = line.replace(i, ' '+ i +' ')
        for i in operators:
            line = line.replace(i, ' '+ i +' ')
        for i in logicalops:
            line = line.replace(i, ' '+ i +' ')
        line = line.split(' ')

        if line[0] in varini:
            temp = line[1:-2]
            for i in temp:
                if (i.isalpha()):
                    identifiers.append(i)
            keywords.append(line[0])
        if line[0] in syntaxWords:
            keywords.append(line[0])

        for i in operators:
            if i in line:
                if i not in mathoperator:
                    mathoperator.append(i)

        for i in logicalops:
            if i in line:
                if i not in logicaloperator:
                    logicaloperator.append(i)

        for i in otherstuffs:
            if i in line:
                if i not in others:
                    others.append(i)

        for i in line:
            try:
                float(i)
                if i not in numericalvalues:
                    numericalvalues.append(i)
            except ValueError:
                continue

        for i in line:
            if i.isnumeric() and i not in numericalvalues:
                    numericalvalues.append(i)

print("Keywords: ",*keywords, sep = ' ')
print("Identifiers: ", *identifiers, sep = ' ')
print("Math Operators: ",*mathoperator, sep = ' ')
print("Logical Operators: ",*logicaloperator, sep = ' ')
print("Numerical Values: ",*numericalvalues, sep = ' ')
print("Others: ", *others, sep = '')
