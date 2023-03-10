fileInput= open("input1.txt")
fileoutput = open("output2.txt" ,"w")

data = int(fileInput.readline())
lists = []

for i in fileInput:
    val = list(map(str,i.strip().split(" ")))
    lists.append(val)

graph={}
for i in range(data):
    list = lists[i]
    graph[list[0]] = list[1:]

visited = []
queue = []

def bfs(visited, graph, node, endPoint):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end = ' ', file = fileoutput)

        if m == endPoint:
            break

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, '1', '12')
