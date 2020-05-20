
# def test_smth(arg1, arg2, arg3=5):
#     return (arg1, arg2, arg3)
#
# r = test_smth(5, arg3=1, arg2=10)


#* в объявлении аргумента указывает на переменное количество аргументов
#* вне объявления аргументов функции отвечает за распаковку структур [1, 2, 3, 4,] => 1 2 3 4


def my_sum(arg1, *args, default_1=None, **kwargs):
    s = 0
    print(kwargs)
    print(default_1)
    for number in args:
        s += number
    return s


list_of_numbers = (6, 100, 22, 4, 2, 2, 3, 4, 5, 12, 2.5, 3, 100)
dict_of_data = {'four': 4, 'six': 6, 'eight': 8}

#r = my_sum(*list_of_numbers, four=4, six=6, eight=9)
# Тоже самое что снизу, но с распаковкой словаря
r = my_sum(*list_of_numbers, default_1=4, **dict_of_data)


print(r)