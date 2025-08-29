l = [9,3,19,12,55]
l.sort()

def binary(st, end, num):
    
    while (end >= st):
        mid = (st+end)//2

        if(l[mid] == num):
            return mid
        elif(l[mid] < num):
            st = mid + 1
        else:
            end = mid - 1
    else:
        return -1

num = int(input("Enter the number to search: "))
pos = binary(0, len(l)-1, num)

if(num != -1):
    print(f'{num} is founded at the position {pos+1}')
else:
    print(f"{num} is not founded")