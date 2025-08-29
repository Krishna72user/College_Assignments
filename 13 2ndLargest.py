l = [2, 17, 9, 12, 3]
m = l[0]
n = l[0]

i = 0
while(i<len(l)):
    if(l[i] > m):
        n = m
        m = l[i]
    elif(l[i] < m and l[i] > n):
        n = l[i]
    i += 1

print("The second largest number is", n)