# 1. встроенные модули
import random
import os
import sys
import shutil
# 2. наши модули
import famous_persons
# 3. сторонние модули
import django
import numpy

# os - основные функции
# путь до текущей папки
print(os.getcwd())

# список файлов и папок
print(os.listdir())

for i in range(5):
    # проверка на существование
    if not os.path.exists(f'new{i}'):
        # сздать папку передаем путь
        os.mkdir(f'new{i}')

for i in range(5):
    # удалить папку
    os.rmdir(f'new{i}')

# соединение путей
path = os.path.join(os.getcwd(), 'main', 'other', 'file.txt')
print(path)

# shutil
shutil.copy('famous_info.py', 'famous_info_copy.py')

# sys
print(sys.platform)
# Это пути где питон ищет файлы
print(sys.path)

# sys.path.remove('/home/dante/Документы/NU/NU5Модули/Задание дз/lesson5modules')
# sys.path.remove('/home/dante/Документы/NU/NU5Модули/Задание дз/lesson5modules')
print(sys.path)
sys.path.append('/home/dante/')
print(sys.path)
import hello

print(sys.executable)

import random
import math
import functools
import glob