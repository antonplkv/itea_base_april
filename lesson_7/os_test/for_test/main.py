import os
import random


def seed_directory(number_of_files, ext):

    for _ in range(number_of_files):
        open(f'{random.randint(0, 1000)}.{ext}', 'w').close()


def clean_directory(directory_path='.', exclude_filename='main.py'):
    files = os.listdir(directory_path)

    for file in files:
        if file != exclude_filename:
            os.remove(file)

# print(os.getcwd())
# seed_directory(4, 'txt')


clean_directory()


