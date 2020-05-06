y = 50


def my_function():
    x = 10
    print(x)


def my_function_2():
    global y
    y += 10
    print(y)


print(y)
my_function_2()
print(y)