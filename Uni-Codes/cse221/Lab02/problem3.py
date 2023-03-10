fileIn = open("input3.txt")
fileOut = open("output3.txt", "w")

inputFile = fileIn.read().split()
inputFile = list(map(int, inputFile))

n = inputFile[0]
arrayA = inputFile[1:n+1]
arrayB = inputFile[n+1::]

def insertion_sort(arrayA, arrayB):
    for i in range(1, n):

        key = arrayB[i]
        key1 = arrayA[i]
        index = i-1

        while index >= 0 and key <= arrayB[index]:
            arrayB[index + 1] = arrayB[index]
            arrayA[index + 1] = arrayA[index]
            index -= 1

        arrayB[index + 1] = key
        arrayA[index + 1] = key1

insertion_sort(arrayA, arrayB)
arrayA.reverse()

for i in arrayA:
    print(f"{i} ", end=" ", file=fileOut)
