
file = open('../lesson_4/for_loop.py', 'r', encoding='utf-8')

#Чтение из файла
for line in file:
    print(line.strip())

# r = file.readlines()
# print(r)

# for i in range(10,20):
#     file.write(str(i))




file.close()

