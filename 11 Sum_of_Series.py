def series(num):
    if(num == 0):
        return 0
    result = ((-1)**(num+1)*num**2) + series(num-1)
    return result

num = int(input("Enter n: "))
result = series(num)
print("The computed value is", result)