l = [[1,0,0],[0,4,0],[0,0,1]]
flag = True

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
    print("The matrix is an identity matrix")
else:
    print("The matrix is not an identity matrix")