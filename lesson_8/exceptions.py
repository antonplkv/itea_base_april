
try:
    number1 = float(input('Введите делимое'))
    number2 = float(input('Введите делитель'))

except ValueError:
    print('Вы ввели неверные данные. Ваши данные были заменены на единицы')
    number1, number2 = 1, 1


try:
    result = number1 / number2
except ZeroDivisionError:
    result = number1
except TypeError:
    result = number1
    print('Ошибка типов!!!!')

print(result)