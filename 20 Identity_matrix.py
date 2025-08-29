l = [[],[],[]]
flag = True
n = len(l)

def matrixInp(matrix):
    for i in range(n):
        matrix[i] = list(map(int, input("Enter elements: ").split()))

print("Enter elements row by row: ")
matrixInp(l)

for i in range(3):
    for j in range(3):
        if(i == j):
            if(l[i][j] != 1):
                flag = False
                break
        else:
            if(l[i][j] != 0):
                flag = False
                break
    if(not flag):
        break

if(flag):
    print("\nThe matrix is an identity matrix")
else:
    print("\nThe matrix is not an identity matrix")