fileInput = open("input2.txt")
fileoutput = open("output2.txt", "w")
data = fileInput.readline().split()

N, M = int(data[0]), int(data[1])
inputlist = []

for i in fileInput:
    val = list(map(int, i.strip().split(" ")))
    inputlist.append(val)

def MaximumActivites(inputlist,n,m):
    lists = sorted(inputlist, key=lambda a: a[1])
    selected=[]
    f=[]

    for i in range(m):
        selected.append(lists[i])
        f.append(lists[i][1])

    for i in range(m, n):
        for j in range(m):
            if lists[i][0] >= f[j]:
                f[j] = lists[i][1]
                selected.append(lists[i])
                break

    print(len(selected), file = fileoutput)

MaximumActivites(inputlist, N, M)
