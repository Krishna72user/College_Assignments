def sumdigit(num):
    sum = 0
    while(num != 0):
        sum += num%10
        num //= 10
    return sum

def proddigit(num):
    prod = 1
    while(num != 0):
        prod *= num%10
        num //= 10
    return prod

num = int(input("Enter the number: "))
if(sumdigit(num) == proddigit(num)):
    print(num, "is a spy number")
else:
    print(num, "is not a spy number")