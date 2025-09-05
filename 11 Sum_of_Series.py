def series(num):
    if not num: return 0
    val =(num-1)**2-(num)**2
    return val + series(num-2)
    

num = int(input("Enter n: "))
result = series(num)
print("The computed value is", result)