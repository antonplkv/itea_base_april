import time

# t = time.time()
#
# print(time.ctime(t))
#
# date_struct = time.localtime()
#
# formatted = time.strftime('Number %d Month number %m year %y', date_struct)
# print(formatted)


# print('Hello')
# time.sleep(5)
# print('World')

a = 5
b = 10


def number_func(a, b):
    return any([a == b, abs(a-b) == 5, a + b == 5])
