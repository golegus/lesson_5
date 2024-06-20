import os
import shutil
import sys

def print_items(msg,items):
    print(msg)
    for item in items:
         print(f"{items.index(item)} - {item}")

def list_dir():
    items=[]
    for item in os.listdir():
        items.append(item)
    return items

def is_file(item):
    items=list_dir()
    current_directory = os.getcwd()
    if os.path.isfile(os.path.join(current_directory, items[item])):
        return True
    elif os.path.isdir(os.path.join(current_directory, items[item])):
        return False
    
def list_files():
    files=[]
    current_directory = os.getcwd()
    for item in list_dir():
         if os.path.isfile(os.path.join(current_directory, item)):
             files.append(item)
    return files

def list_folders():
    folders=[]
    current_directory = os.getcwd()
    for item in list_dir():
        if os.path.isdir(os.path.join(current_directory, item)):
            folders.append(item)
    return folders

def ask_todo(input_msg):
    items=list_dir()
    print_items("Содержимое текущей папки:",items)
    print ('='*20)
    item=input(input_msg)
    if not item.isdigit():
        print('Ошибка!')
        return False
    else:
        item=int(item)
    if not (0 <= item < len(items)):
        print('Ошибка!')
        return False
    else:
        return item

def new_dir():
    new_dir=input('Введите наименование папки:')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    else:
        print('Ошибка. Такая папка уже существует.')

def rm_dir():
    items=list_dir()
    item=ask_todo('Введите номер элемента для удаления: ')
    if item ==False:
        return
    if is_file(item) :
        os.remove(items[item])
    else:
        os.rmdir(items[item])
    items=list_dir()
    print_items("Содержимое текущей папки:",items)

def copy_item():
    items=list_dir()
    item=ask_todo('Введите номер элемента для копирования: ')
    if item == False:
        return
    new_name=input(f"Введите имя элемента для копирования {items[item]}: ")
    if is_file(item):
        shutil.copy(items[item], new_name)
    else:
        shutil.copytree(items[item], new_name)
    print_items("Содержимое текущей папки:", list_dir())