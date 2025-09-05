n = int(input("Enter n : "))
a,b = (0,1)
print("\nThe Fibonacci series is: ")
if n>=2:
    print(a,b,end=" ")
    for _ in range(n-2):
        c = a+b
        print(c,end=" ")
        a=b
        b=c
else: print(0)