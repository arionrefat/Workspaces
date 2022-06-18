file = open("input.txt")
file2 = file.read().splitlines()
file.close()
graph = [[]]

for i in range(len(file2)):
    for j in range(len(file2[0])):
        if file2[i][j] != " ":
            graph[i].append(file2[i][j])
    if i != len(file2) - 1:
        graph.append([])

max_count = 0
row = len(graph)
col = len(graph[0])


def dfs(graph, i, j):
    if i >= 0 and i < row and j >= 0 and j < col and graph[i][j] == "Y":
        graph[i][j] = "N"
        count = 1
        count += dfs(graph, i - 1, j)
        count += dfs(graph, i + 1, j)
        count += dfs(graph, i, j - 1)
        count += dfs(graph, i, j + 1)
        count += dfs(graph, i - 1, j + 1)
        count += dfs(graph, i - 1, j - 1)
        count += dfs(graph, i + 1, j - 1)
        count += dfs(graph, i + 1, j + 1)
        return count

    else:
        return 0


for i in range(row):
    for j in range(col):
        if graph[i][j] == "Y":
            max_count = max(max_count, dfs(graph, i, j))

print(max_count)
