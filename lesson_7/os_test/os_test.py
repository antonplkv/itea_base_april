import os

print('Start working directory')
print(os.getcwd())

print()

print('Current working directory files')
print(os.listdir())



os.chdir('../lesson_6')

print('New working directory')
print(os.getcwd())

print('New working directory files')
print(os.listdir())
