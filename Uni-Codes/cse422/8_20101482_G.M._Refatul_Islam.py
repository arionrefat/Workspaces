# ------------------------------------- Task 1-----------------------
"""
input needs to be like this

N N N Y Y N N
N Y N N Y Y N
Y Y N Y N N Y
N N N N N Y N
Y Y N N N N N
N N N Y N N N

"""
fileIn = open("input.txt")
inputFile = fileIn.readlines()
fileIn.close()
inputFile = list(inputFile)
inputGraph = []
visitedNodes = []
total_infected = 0

for e in inputFile:
    if "\n" in e:
        s = e.strip().split()
        inputGraph.append(s)
    else:
        s = e.split()
        inputGraph.append(s)

    for i in range(len(s)):
        if "Y" in s[i]:
            s[i] = 1
        else:
            s[i] = 0


def dfs(i, j, count):
    try:
        if inputGraph[i][j + 1] == 1 and i + j + 1 not in visitedNodes:
            visitedNodes.append(i + j + 1)
            count = dfs(i, j + 1, count + 1)
    except IndexError:
        pass

    if j and inputGraph[i + 1][j - 1] == 1 and i + 1 + j + 1 not in visitedNodes:
        visitedNodes.append(i + 1 + j - 1)
        count = dfs(i + 1, j - 1, count + 1)

    try: # Pycharm added the following try catch as code action
        if inputGraph[i + 1][j] == 1 and i + 1 + j not in visitedNodes:
            visitedNodes.append(i + 1 + j)
            count = dfs(i + 1, j, count + 1)
    except IndexError:
        pass

    try:
        if inputGraph[i + 1][j + 1] == 1 and (i + 1 + j + 1) not in visitedNodes:
            visitedNodes.append(i + 1 + j + 1)
            count = dfs(i + 1, j + 1, count + 1)
    except IndexError:
        pass

    return count


for i, row in enumerate(inputGraph):
    for j, _ in enumerate(row):
        count = 0
        if inputGraph[i][j] == 1:
            if i + j not in visitedNodes:
                visitedNodes.append(i + j)
                total_infected = max(total_infected, dfs(i, j, count + 1))

print("maximum infected area : ", total_infected)

# ----------------------------------------------- Task 2 ------------------------------

"""
input needs to be like this
3
3
A H H
T H H
H T H
"""

fileIn = open("input2.txt")
fileIn.readline()
fileIn.readline()
inputFile = fileIn.readlines()
fileIn.close()
inputFile = list(inputFile)

inputGraph = []
stack = []

for e in inputFile:
    if "\n" in e:
        s = e.strip().split()
        inputGraph.append(s)
    else:
        s = e.split()
        inputGraph.append(s)


def bfs():
    time = -1
    while stack:
        leng = len(stack)
        for _ in range(leng):
            nodeCurrent = stack.pop(0)
            i = int(nodeCurrent[0])
            j = int(nodeCurrent[1])

            if i and "H" in inputGraph[i - 1][j]:
                inputGraph[i - 1][j] = "A"
                stack.append(str(i - 1) + str(j))

            if j and "H" in inputGraph[i][j - 1]:
                inputGraph[i][j - 1] = "A"
                stack.append(str(i) + str(j - 1))

            try:
                if "H" in inputGraph[i + 1][j]:
                    inputGraph[i + 1][j] = "A"
                    stack.append(str(i + 1) + str(j))
            except IndexError:
                pass

            try:
                if "H" in inputGraph[i][j + 1]:
                    inputGraph[i][j + 1] = "A"
                    stack.append(str(i) + str(j + 1))
            except IndexError:
                pass

        time += 1
    return time


for i, row in enumerate(inputGraph):
    for j, column in enumerate(row):
        if "A" in column:
            if str(i) + str(j) not in stack:
                stack.append(str(i) + str(j))

print(f"Time: {bfs()} minutes")

survived = 0
if any("H" in x for x in inputGraph):
    survived += 1

print(f"{survived} survived") if survived > 0 else print("No one survived")
