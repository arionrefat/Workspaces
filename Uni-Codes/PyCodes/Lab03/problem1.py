fileInput= open("input1.txt")
fileoutput = open("output1.txt" ,"w")

data = int(fileInput.readline())
lists = []

for i in fileInput:
    val = list(map(str,i.strip().split(" ")))
    lists.append(val)

graph={}
for i in range(data):
    list1 = lists[i]
    graph[list1[0]] = list1[1:]

print(graph)
