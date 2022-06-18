fileIn = open("input.txt")
inputFile = fileIn.readlines()
fileIn.close()
inputFile = list(inputFile)

table = []
visited = []

for e in inputFile:
    if "\n" in e:
        s = e.strip().split()
        table.append(s)
    else:
        s = e.split()
        table.append(s)

    for i in range(len(s)):
        if "Y" in s[i]:
            s[i] = 1
        else:
            s[i] = 0


def dfs(row, column, count):
    if table[row][column + 1] == 1:
        if row + column + 1 not in visited:
            visited.append(row + column + 1)
            count = dfs(row, column + 1, count + 1)

    if column != 0:
        if table[row + 1][column - 1] == 1:

            if row + 1 + column + 1 not in visited:
                visited.append(row + 1 + column - 1)
                count = dfs(row + 1, column - 1, count + 1)

    # checking (x+1, y) down position for child
    if table[row + 1][column] == 1:
        if row + 1 + column not in visited:
            visited.append(row + 1 + column)
            count = dfs(row + 1, column, count + 1)

    # checking (x+1, y+1) diagonal position for child

    if table[row + 1][column + 1] == 1:

        if row + 1 + column + 1 not in visited:
            visited.append(row + 1 + column + 1)
            count = dfs(row + 1, column + 1, count + 1)


    return count

    # traverse the table


for row in range(len(table)):
    for column in range(len(table[row])):
        count = 0
        # if find Y in the table applying DFS

        if table[row][column] == 1:
            if row + column not in visited:
                visited.append(row + column)
                count = dfs(row, column, count + 1)
                print(count)

print("maximum infected area : ", count)
