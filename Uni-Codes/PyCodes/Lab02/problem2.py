fileIn = open("input2.txt")
fileOut = open("output2.txt", "w")

inputFile = fileIn.read().split()
inputFile = list(map(int, inputFile))

n = inputFile[0]
m = inputFile[1]
A = inputFile[2::]

for i in range(len(A)):

    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j

    A[i], A[min_index] = A[min_index], A[i]

for i in range(m):
    print(f"{A[i]} ", end = " ", file=fileOut)
