list_1 =[10,20,30,50,40,10]
for i in list_1:
    if list_1.count(i)>1:
        list_1.remove(i)
print(list_1)