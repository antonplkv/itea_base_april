#Реализация с помощью циклов
my_list = [1, 2, 3, 4, 5, 6, 7]

my_list_of_squares = []

for i in my_list:
    my_list_of_squares.append(i ** 2)

print(my_list_of_squares)


#Реализация с помощью ламбды
# def get_list():
#
#     return my_list

my_list = [1, 2, 3, 4, 5, 6, 7]


# Можно использовать вместо лямбды
# def to_square(number):
#     return number ** 2

result = list(map(lambda n: n ** 2, my_list))

print(result)


############FILTER###########


#Реализация с помощью циклов
new_sequence = [1, 100, 3, 40, 6, 120]
greater_than_50 = []

for number in new_sequence:
    if number > 50:
        greater_than_50.append(number)
print(greater_than_50)

#filter

# Вместо лямбды
# def is_greater_than_50(number):
#     return number > 50


result = filter(lambda n: n > 50, new_sequence)
print(list(result))


