def almost_double_factorial(n):
    num = 1
    for x in range(1, n+1, 2):
        num = num * x
    return num
