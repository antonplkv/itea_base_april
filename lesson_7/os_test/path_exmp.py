import os

file_path = r'C:\Users\Anton\PycharmProjects\itea_base_april\lesson_7\os_test.py'

file_name = os.path.basename(file_path)

dir_path = os.path.dirname(file_path)

#print(os.path.join(file_name, dir_path))
#print(os.path.exists(file_path))

print(os.path.isfile(file_path))

print(os.path.split(file_path))


