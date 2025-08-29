n = int(input("Enter number: "))

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if(num%i == 0):
            return False
    return True

print("The prime factors of", n, "is/are: ", end="")
for i in range(2, n//2+1):
    if(n%i == 0 and isPrime(i)):
        print(i, end=' ')

if(isPrime(n)):
    print(n)