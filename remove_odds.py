list_1 = [1,7,3,5,4,8]
l = len(list_1)
i=0

while(i<l):
    if(list_1[i] % 2 != 0):
        list_1.remove(list_1[i])
        i = i-1
        l = len(list_1)
    else:
        i+=1

print(list_1)