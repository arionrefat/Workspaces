fileIn = open("input1.txt")
fileOut = open("output1.txt", "w")

inputFile = fileIn.read().split()
inputFile = list(map(int, inputFile))

n = inputFile[0]
array = inputFile[1::]

def bubbleSort(arr):
    global n

    # Traversing through all the elements in the array
    for i in range(n):
        isSwitched = False

        for j in range(0, n-i-1):
            #traversing the array within range 0 to n-i-1 and then swaping them if that element is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwitched = True
        # If no two of these elements were swapped inside the inner loop, then the whole loop will break thus making the time complexity O(n) and this will be the best case senario
        if isSwitched == False:
            break

bubbleSort(array)
for i in range(len(array)):
    print (array[i],end=" ",file=fileOut)
