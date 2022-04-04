syntaxWords = ["if", "else", "for"]
varini = ["int", "double", "float"]
operators = ["+", "-", "="]
logicalops = [">"]
otherstuffs = [",", "(", ")", ";", "{", "}"]

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
            line = line.replace(i, " " + i + " ")
        for i in operators:
            line = line.replace(i, " " + i + " ")
        for i in logicalops:
            line = line.replace(i, " " + i + " ")
        line = line.split(" ")

        for i in line:
            if i in syntaxWords or i in varini and i not in keywords:
                keywords.append(i)

            elif i in operators and i not in mathoperator:
                mathoperator.append(i)

            elif i in logicalops and i not in logicaloperator:
                logicaloperator.append(i)

            elif i in otherstuffs and i not in others:
                others.append(i)

            elif (
                i not in syntaxWords
                and i not in operators
                and i not in logicalops
                and i not in otherstuffs
            ):
                try:
                    float(i)
                    if i not in numericalvalues:
                        numericalvalues.append(i)
                except ValueError:
                    pass

                if i.isdigit() and i not in numericalvalues:
                    numericalvalues.append(i)

                elif i not in numericalvalues and i not in identifiers:
                    identifiers.append(i)

print("Keywords: ", *keywords, sep=" ")
print("Identifiers: ", *identifiers, sep=" ")
print("Math Operators: ", *mathoperator, sep=" ")
print("Logical Operators: ", *logicaloperator, sep=" ")
print("Numerical Values: ", *numericalvalues, sep=" ")
print("Others: ", *others, sep="")
