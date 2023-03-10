fileInput= open("/home/refat/Workspaces/Uni-Codes/PyCodes/Lab03/input1.txt")
fileoutput = open("/home/refat/Workspaces/Uni-Codes/PyCodes/Lab03/output3.txt" ,"w")

data = int(fileInput.readline())
lists = []

for i in fileInput:
    val = list(map(str,i.strip().split(" ")))
    lists.append(val)

graph={}
for i in range(data):
    list = lists[i]
    graph[list[0]] = list[1:]

print(graph)

visited = []

def dfs_visit(graph, node):
    for v in graph[node]:
        if v not in visited:
            visited.append(v)
            dfs_visit(graph, v)


def dfs(graph, endPoint):
    for v in [*graph]:
        if v not in visited:
            visited.append(v)
            dfs_visit(graph, v)

dfs(graph, '12')

for v in visited:
    if (v == '12'):
        print(v, end = '', file=fileoutput)
        break
    print(v, end = ' ', file=fileoutput)
