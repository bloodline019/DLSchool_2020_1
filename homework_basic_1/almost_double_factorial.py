def almost_double_factorial(n):
    out = 1
    for i in range(1,n+1,2):
        out *= i
    return out
