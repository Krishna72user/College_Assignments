list_1 = [7,4,2,6,8,9]
l = len(list_1)
i=0

while(i<l):
    if(list_1[i] % 2 != 0):
        list_1.remove(list_1[i])
        l = len(list_1)
    else:
        i+=1

print(list_1)