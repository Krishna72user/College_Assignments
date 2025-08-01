tup = (30,50,20,10,80,60)
list_1 = list(tup)
def sort_by_last(n):
    return abs(60-n)
list_1.sort(key = sort_by_last)
tup = tuple(list_1)
print(tup)
