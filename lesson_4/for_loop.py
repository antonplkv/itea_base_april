# test_str = 'mystring'
#
# for i in test_str:
#     print(i, end='')
#
# print()
#
#
test_dict = {'milk': 20, 'meat': 90, 'tomato': 20}


values_list = []
for i in test_dict.items():
    print(i)


# for i in range(300):
#     print(i)
#
# list_my = [1, 2, 3]

a = 5
b = 10
c = 20
d = 30
(a, b, c, d) = (b, a, d, c)
print(a, b, c, d)
# temp = b
# b = a
# a = temp
#
#

my_tuple = (1, 2, 3)

# Это
# a = my_tuple[0]
# b = my_tuple[1]
# c = my_tuple[2]

# Равносильно этому
a, b, c = my_tuple

my_list_of_tuples = [(1, 2), (2, 3)]

for a, b in my_list_of_tuples:
    print(a, b)


test_dict = {'milk': 20, 'meat': 90, 'tomato': 20}

values_list = []
for k, v in test_dict.items():
    print(k, v)


my_list = [5, 2, 3, 40, 50, 12]


for idx, value in enumerate(my_list):
    print(idx, value)
