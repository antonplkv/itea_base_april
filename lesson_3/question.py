def myf(n):
    num = 1
    while num >= 1:
        num = num * n
        n = n - 1
    print(num)
    return num


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    print(num)
    return num


myf(10)
factorial(10)