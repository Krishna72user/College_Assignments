list_1 =[10,20,20,20,20,10]

length = len(list_1)
i = 0
while(i<length):
    print(i)
    if list_1.count(list_1[i])>1:
        list_1.remove(list_1[i])
        length = len(list_1)
    else:
        i = i+1
    
print(list_1)