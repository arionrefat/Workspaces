fileInput = open("input1.txt")
fileoutput = open("output1.txt", "w")

data = fileInput.readline()
n = int(data[0])
inputlist = []

for i in fileInput:
    val = list(map(int, i.strip().split(" ")))
    inputlist.append(val)


def AssignmentSelection(inputlists, n):
    lists = sorted(inputlists, key=lambda a: a[1])
    selected = []
    selected.append(lists[0])
    count = 1
    count1 = 1
    f = lists[0][1]

    for i in range(1, n):
        if lists[count1][0] >= f:
            count += 1
            f = lists[count1][1]
            selected.append(lists[count1])
        count1 +=1
    print(count, file = fileoutput)

    for i in range(len(selected)):
        for j in range(len(selected[i])):
            print(selected[i][j], end=' ', file = fileoutput)
        print(file = fileoutput)

AssignmentSelection(inputlist, n)
