l = [0, 1]
i = 2
n = int(input("Enter the nth term: "))

while(i<=n):
    fibo = l[i-1] + l[i-2]
    l.append(fibo)
    i += 1

i = 0
print("\nThe Fibonacci series is: ")
while(i < len(l)):
    print(l[i], end=" ")
    i += 1