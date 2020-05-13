# def get_fullname(name, surname):
#     return f'{name.capitalize()} {surname.capitalize()}'
#
#
#
# print(get_fullname('anton', 'polyakov'))
# new_function = get_fullname
# print(new_function)
# new_function = get_fullname
# print(new_function('anton', 'polyakov'))


# def test_func(f, message):
#     f()
#     print(message)
#
#
# def hello_world():
#     print('Hello world')
#
#
# def bye_world():
#     print('Bye world')
#
# test_func(bye_world, 'Hi')


def func1():
    print('Hi')


def func2():
    func1()
    print('Hello')

func2()