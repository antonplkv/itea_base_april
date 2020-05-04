# my_list = [1, 2, 3, 4, 5, 6]
# print(my_list[-6])
#
# i = 5
# my_list = [1, 2, 3, 4, 5, 6]
#
# while i >= 0:
#     print(my_list[i])
#     i -= 1
#
#
#break
#
# numbers = (2, 2, 3, 3, 4, 5, 4, 5, 10, 2, 30, 40)
# i = 0
# length_of_tuple = 12
# matches = 0
#
# while i < length_of_tuple:
#     element = numbers[i]
#     print(i)
#     if element == 2:
#         matches += 1
#         if matches > 2:
#             break
#     i += 1
#
#
# if matches > 2:
#     print(f'Количество совпадений больше двух')

#continue

a = [1, 2, 2, 2, 2, 2, 6, 4, 3]
i = 0
len_of_a = 9

while i < len_of_a:
    elem = a[i]
    i += 1

    if elem == 2:
        continue
    print(elem)



