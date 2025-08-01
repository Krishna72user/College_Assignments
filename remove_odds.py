list_1 =[1,7,3,5,4,8]
for i in list_1:
    print(i)
    if i%2!=0:
        list_1.remove(i)
print(list_1)
