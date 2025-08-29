l1 = [2, 5, 7, "apple", 5.8, "orange"]
l2 = [4, 8, "banana", "apple", 7]

i = 0
j = 0
while(i<len(l1)):
    flag = j = 0
    while(j<len(l2)):
        if(l1[i] == l2[j]):
            flag = 1
        j += 1
    
    if(flag == 1):
        l1.remove(l1[i])
    else:
        i+=1

print("The subtracted list is:", l1)