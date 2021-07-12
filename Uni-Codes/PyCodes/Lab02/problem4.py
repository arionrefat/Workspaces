fileIn = open("input4.txt")
fileOut = open("output4.txt", "w")

inputFile = fileIn.read().split()
inputFile = list(map(int, inputFile))

n = inputFile[0]
array = inputFile[1::]

def merge(left, right):
    outcome = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            outcome.append(left[i])
            i += 1
        else:
            outcome.append(right[j])
            j += 1

    outcome += left[i:]
    outcome += right[j:]
    return outcome

def mergesort(elements):
    if (len(elements) <= 1):
        return elements

    mid = int(len(elements)/2)
    left = mergesort(elements[:mid])
    right = mergesort(elements[mid:])
    return merge(left,right)

for i in mergesort(array):
    print(f"{i} ", end = " ", file=fileOut)
