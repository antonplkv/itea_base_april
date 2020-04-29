secret_number = 86

start_range = 0
end_range = 20

user_number = int(input(f'Угадайте целое число в диапазоне от {start_range} до {end_range}'))

if user_number == secret_number and start_range <= user_number <= end_range:
    print('Поздравляем, вы ввели верное число')
elif user_number != secret_number and start_range <= user_number <= end_range:
    print('Вы ввели неверное число')
    if user_number < secret_number:
        print('Число должно быть больше')
    elif user_number > secret_number:
        print('Число должно быть меньше')
else:
    print('Число не входит в диапазон. ')
