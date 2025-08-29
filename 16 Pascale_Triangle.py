def fact(n):
    if(n == 0):
        return 1
    return n*fact(n-1)

def combination(n, r):
    q = fact(n)
    p = fact(n-r) * fact(r)
    return q//p

# Main Function
row = int(input("Enter the number of rows: "))
for i in range(row):
    for j in range(row-i-1):
        print(' ', end='')
    for k in range(i+1):
        print(combination(i, k), end=' ')
    print()