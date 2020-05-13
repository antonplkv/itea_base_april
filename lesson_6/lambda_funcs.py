def my_func_high_level(func):
    r = func(30, 40)
    return r


result = my_func_high_level(lambda a, b: a + b)
print(result)

lambda a, b: a + b

def my_sum(a, b):
    return a + b