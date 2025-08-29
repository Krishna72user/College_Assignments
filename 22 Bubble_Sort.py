n = int(input("Enter the number of elements: "))
l = []

def bubble(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if(l[j] > l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

print("\nEnter elements one-by-one: ")
for _ in range(n):
    x = int(input("Enter element: "))
    l.append(x)

bubble(l)
print(l)