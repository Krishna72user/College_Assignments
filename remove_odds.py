list_1 = [2,3,2,6,8,9]
l = len(list_1)
i=0

print(list_1)
while(i<l):
    print(i)
    if(list_1[i] % 2 != 0):
        list_1.remove(list_1[i])
        l = len(list_1)
    else:
        i+=1

print(list_1)