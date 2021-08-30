fileInput = open("input1.txt")
fileoutput = open("output1.txt", "w")
n = int(fileInput.readline())
string1 = fileInput.readline()
string2 = fileInput.readline()

def LCS(X, Y, N):
    m = N
    n = N

    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                L[i][j] = 0

            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1

            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    lcs = L[m][n]
    zoneLCS = [''] * (lcs+1)
    i, j = m, n

    for num in range(N + 2):
        if (i < 0 and j < 0 ):
            break

        if X[i-1] == Y[j-1]:
            zoneLCS[lcs-1] = X[i-1]
            i -= 1
            j -= 1
            lcs -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1

        else:
            j -= 1

    print(zoneLCS)

    zoneLCS.remove('')

    zoneNames = {'Y' : 'Yasnaya', 'P' : 'Pochinki', 'S' : 'School', 'R' : 'Rozhok', 'F' : 'Farm', 'M' : 'Mylta', 'H' : 'Shelter', 'I' : 'Prison'}

    for i in zoneLCS:
        print(zoneNames.get(i), end = ' ', file = fileoutput)

    print(file = fileoutput)

    print('Correctness of prediction: ', int((L[m][n]*100)/N), '%', file = fileoutput)

LCS(string1, string2, n)
