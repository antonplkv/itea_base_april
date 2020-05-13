# def test_func():
#
#     print(' i am outer function')
#
#     def inner_func():
#         print('I am inner function')
#
#     def one_more_inner_func():
#         print('Hello i am one more inner function')
#
#     return inner_func, one_more_inner_func
#
#
# functions = test_func()
# functions[0]()
# functions[1]()


#Функция декоратор (имя произвольное)
def decorator(func):
    #func - объект целевой функции, в нашем случае это функция start

    #имя произвольное (принято использовать wrapper)
    def wrapper(arg1):
        print(arg1)
        #Враппер должен принимать тоже самое количество аргументов
        #которое принимает целевая функция
        #Измененная целевая функция
        print('decorating function')
        result = func(arg1)#Целевая функция приинт (не забываем передавать в нее аргументы)
        print('Decoration ended')

        #Возвраемое значение целевой функции определяется внутри враппера
        return result

    #Функция декоратор должна возвращать объект враппер
    return wrapper


#Целевая функция
@decorator
def start(arg1):
    print('Function has been started')
    return 12

b = start(10)
print(b)