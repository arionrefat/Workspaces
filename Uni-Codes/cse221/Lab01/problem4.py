fileIn = open("input4.txt")
fileOut = open("output4.txt", "w")

inputFile = fileIn.read().split()
inputFile = list(map(int, inputFile))

n = inputFile[0]
matrixListA = inputFile[1:10]
matrixListB = inputFile[10::]

matrixInitial = [[0]*(n) for i in range(n)]

def List3D(list1,rows, columns):
    result=[]
    start = 0
    end = columns
    for i in range(rows):
        result.append(list1[start:end])
        start += columns
        end += columns
    return result

matrixA = List3D(matrixListA, n, n)
matrixB = List3D(matrixListB, n, n)

for i in range(n):
    for j in range(n):
        for k in range(n):
            matrixInitial[i][j] += matrixA[i][k]*matrixB[k][j]

for i in matrixInitial:
    for j in i:
        print(f"{j} ", file = fileOut)
    print("\n", file=fileOut)
