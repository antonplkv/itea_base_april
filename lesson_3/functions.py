# def get_max(a, b):
#     if a < b:
#         print('A меньше b')
#     elif a > b:
#         print('А больше б')
#     elif a == b:
#         print('А и б равны')
#     else:
#         print('Случилась оишбка.')
#
# print('Hi')
#
# first_argument = 30
# second_argument = 20
# get_max(first_argument, second_argument)
# print('Hello')

PI = 3.1415

def factorial(n):
    num = 1

    while n >= 1:
        num = num * n
        n = n - 1
    print(num)
    return num



def print_list(my_list):
    for i in my_list:
        print(i)

factorial(5)
a = [1, 2, 3, 4,5]
print_list(a)

