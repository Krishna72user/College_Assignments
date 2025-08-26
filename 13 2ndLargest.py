l = [2, 7, 9, 12, 3]
m = l[0]
n = l[0]

i = 0
while(i<len(l)):
    if(l[i] > m):
        m = l[i]
    i += 1

i=0
while(i < len(l)):
    if((l[i] > n) and (l[i] < m)):
        n = l[i]
    i += 1

print("The second largest number is", n)