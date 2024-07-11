import os, json
from datetime import datetime 
"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой

"""
def get_current_datetime():
    """
    Возвращаем текущую дату и время с точностью до десятых секунды
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

def create_directory_if_not_exists(directory):
    """
    Создает директорию, если она не существует.
    
    :param directory: Путь к директории.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_json_file(file_path, encoding):
    """
    Читает данные из JSON файла, если файл существует и не пуст.
    
    :param file_path: Путь к JSON файлу.
    :return: Данные из JSON файла или пустой список, если файл не существует или пуст.
    """
    data = []
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r', encoding=encoding) as file:
            data = json.load(file)
    return data

def read_json_file_or_false(file_path, encoding):
    """
    Читает данные из JSON файла, если файл существует и не пуст.
    Возвращает данные, если файл существует, или False, если файл не существует.
    
    :param file_path: Путь к JSON файлу.
    :return: Данные из JSON файла или False, если файл не существует.
    """
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r', encoding=encoding) as file:
            return json.load(file)
    return False

def write_json_file(data, file_path, encoding):
    """
    Записывает данные в JSON файл.
    
    :param file_path: Путь к JSON файлу.
    :param data: Данные для записи в файл.
    """
    with open(file_path, 'w', encoding=encoding ) as file:
        json.dump(data, file, indent=4)

def append_to_json_file(new_data, file_path, encoding):
    """
    Функция для добавления данных в JSON файл. Если файл не существует, он будет создан.
    Возвращает True, если данные успешно добавлены, и False в случае ошибки.
    
    :param file_path: Путь к JSON файлу.
    :param new_data: Новые данные для добавления в JSON файл.
    :return: True если все получилось, False в противном случае.
    """
    directory = os.path.dirname(file_path)
    create_directory_if_not_exists(directory)

    data = read_json_file(file_path, encoding)
    if data is not None:
        data.append(new_data)
        write_json_file(data, file_path, encoding)
        return True
    return False

def add_transaction(amount, file_path='transactions.json', encoding='utf-8'):
    # Получаем текущую дату и время
    current_datetime = get_current_datetime()   
    transaction = {
        "amount": amount,
        "datetime": current_datetime
    }
    append_to_json_file(transaction, file_path, encoding)
    return True


def get_latest_balance(file_path='transactions.json', encoding='utf-8'):
    transactions = read_json_file_or_false(file_path, encoding)
    if transactions:
        return transactions[-1]['amount']
    else:
        return 0  
    
def add_buying_history(name, cost, file_path='expence_history.json', encoding='utf-8'):
    transaction = {
            "name": name,
            "cost": cost
            }
    append_to_json_file(transaction, file_path, encoding)

def get_bying_history(file_path='expence_history.json', encoding='utf-8'):
    data=read_json_file_or_false(file_path, encoding)
    return data

def to_buy(name, cost, expence_file='expence_history.json', transaction_file='transactions.json', encoding='utf-8'):
#   проверяем счет 
    account_balance=get_latest_balance(transaction_file, encoding)
    if account_balance<cost:
        return False
    else:
        add_transaction(account_balance-cost, transaction_file, encoding)
        add_buying_history(name, cost, expence_file, encoding)
        return True

