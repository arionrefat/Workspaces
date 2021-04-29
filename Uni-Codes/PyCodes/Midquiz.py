
A = list()


def FM(n):
    if(A[n] > 0):
        return A[n]
    if(n == 1 or n == 2):
        return 1
    elif(n == 0):
        return 0
    else:
        A[n] = (FM(n-1)+FM(n-2))
        return A[n]


def CalcFib():
    A.insert(0, 1)
    A.insert(1, 1)
    for i in range(2, 46):
        A.insert(i, A[i-1]+A[i-2])

CalcFib()
print(FM(45))
