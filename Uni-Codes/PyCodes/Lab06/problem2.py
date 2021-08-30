fileInput = open("input2.txt")
fileoutput = open("output2.txt", "w")
string1 = fileInput.readline()
string2 = fileInput.readline()
string3 = fileInput.readline()

def lcs(X,Y,Z):
    m = len(X) - 1
    n = len(Y) - 1
    o = len(Z) - 1

    C = [[[None]*(o+1) for i in range(n+1)] for y in range(m+1)]

    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):

                if i == 0 or j == 0 or k == 0 :
                    C[i][j][k] = 0

                elif X[i-1] == Y[j-1] == Z[k-1]:
                    C[i][j][k] = C[i-1][j-1][k-1] + 1

                else:
                    C[i][j][k] = max(C[i-1][j][k] , C[i][j-1][k],C[i][j][k-1])

    return C[m][n][o]

print(lcs(string1, string2, string3), file = fileoutput)

