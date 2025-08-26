A = [[-1,-1,4],[0,3,-3],[2,-1,-2]]
B = [[3,2,3],[2,2,1],[2,1,1]]
C = [[],[],[]]
sum=0
i=j=k=0

while(i<3):
    j=0
    while(j<3):
        sum=0
        k=0
        while(k<3):
            sum += A[i][k] * B[k][j]
            k+=1
        C[i].append(sum)
        j+=1
    i+=1

for i in range(3):
    for j in range(3):
        print(C[i][j], end="  ")
    print()