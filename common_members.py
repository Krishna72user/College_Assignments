list_1 =[100,20,30,50,40,10]
list_2 =[90,25,60,80,40,10]
common=[]
for i in list_1:
    if (i in list_2 and i not in common):
        common.append(i)
print(common)