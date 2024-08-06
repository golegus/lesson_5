import os
import shutil
import sys
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершена")
        return result
    return wrapper

def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print('Ошибка: Ввод должен быть числом')
        except IndexError:
            print('Ошибка: Нет такого пункта')
        except FileNotFoundError:
            print('Ошибка: Файл или директория не существуют.')
        except PermissionError:
            print('Ошибка: Недостаточно прав для выполнения операции.')
        except OSError as e:
            print(f'Ошибка: {e}')
        except Exception as e:
            print(f'Непредвиденная ошибка: {e}')
    return wrapper

@log_decorator
@exception_handler
def print_items(msg, items):
    print(msg)
    for item in items:
        print(f"{items.index(item)} - {item}")

@log_decorator
@exception_handler
def list_dir():
    items = [item for item in os.listdir()]
    return items

@log_decorator
@exception_handler
def is_file(item):
    items = list_dir()
    current_directory = os.getcwd()    
    if os.path.isfile(os.path.join(current_directory, items[item])):
        return True
    elif os.path.isdir(os.path.join(current_directory, items[item])):
        return False

@log_decorator
@exception_handler
def list_files():
    current_directory = os.getcwd()
    files = [item for item in list_dir() if os.path.isfile(os.path.join(current_directory, item))]
    return files

@log_decorator
@exception_handler
def list_folders():
    current_directory = os.getcwd()
    folders = [item for item in list_dir() if os.path.isdir(os.path.join(current_directory, item))]
    return folders

@log_decorator
@exception_handler
def ask_todo(input_msg):
    items = list_dir()
    print_items("Содержимое текущей папки:", items)
    print('=' * 10)
    item = int(input(input_msg))
    selected_item = items[item]
    return item

@log_decorator
@exception_handler
def new_dir():    
    new_dir = input('Введите наименование папки:')
    os.mkdir(new_dir)
    return True

@log_decorator
@exception_handler
def rm_dir():
    items = list_dir()
    item = ask_todo('Введите номер элемента для удаления: ')
    if is_file(item):
        os.remove(items[item])
    else:
        os.rmdir(items[item])
    print(f'Элемент {items[item]} успешно удален')
    items = list_dir()
    print_items("Содержимое текущей папки:", items)
    return True

@log_decorator
@exception_handler
def copy_item():
    items = list_dir()
    item = ask_todo('Введите номер элемента для копирования: ')
    new_name = input(f"Введите имя элемента для копирования {items[item]}: ")
    if is_file(item):
        shutil.copy(items[item], new_name)
    else:
        shutil.copytree(items[item], new_name)
    print_items("Содержимое текущей папки:", list_dir())
    return True

@log_decorator
@exception_handler
def come_to_dir():
    print("Текущий рабочий каталог:", os.getcwd())
    new_directory = input('Введите путь для смены текущего каталога: ')
    os.chdir(new_directory)
    print("Новый рабочий каталог:", os.getcwd())
    return True
