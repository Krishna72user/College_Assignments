A = [[],[],[]]
B = [[],[],[]]
C = [[],[],[]]
n = len(A)
sum=0
i=j=k=0

def matrixInp(matrix):
    for i in range(n):
        matrix[i] = list(map(int, input("Enter elements: ").split()))

print("Enter elements row by row of 1st Matrix: ")
matrixInp(A)

print("\nEnter elements row by row of 2nd Matrix: ")
matrixInp(B)

while(i<n):
    j=0
    while(j<n):
        sum=0
        k=0
        while(k<n):
            sum += A[i][k] * B[k][j]
            k+=1
        C[i].append(sum)
        j+=1
    i+=1

print("\nThe multiplication of the matrices: ")
for i in range(n):
    for j in range(n):
        print(C[i][j], end="  ")
    print()