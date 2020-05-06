a = [5, 10, 4, 2]


for i in range(len(a)):
    print(a[i])


for i in a:
    print(i)


def is_equal_5(a, b):
    if abs(a - b) == 5:
        return True


print(is_equal_5(10, 5))
print(is_equal_5(5, 10))

