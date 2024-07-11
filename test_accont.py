import pytest
import os
import json
from datetime import datetime
from utils.acc_func import (
    get_current_datetime,
    create_directory_if_not_exists,
    read_json_file,
    read_json_file_or_false,
    write_json_file,
    append_to_json_file,
    add_transaction,
    get_latest_balance,
    add_buying_history,
    get_bying_history,
    to_buy
)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              #     return tmpdir

# Тест для get_current_datetime
def test_get_current_datetime():
    current_datetime = get_current_datetime()
    assert isinstance(current_datetime, str)
    datetime.strptime(current_datetime, '%Y-%m-%d %H:%M:%S.%f')

# Тест для create_directory_if_not_exists
def test_create_directory_if_not_exists(tmpdir):
    test_dir = tmpdir.mkdir("test_dir")
    dir_path = os.path.join(test_dir, "new_dir")
    create_directory_if_not_exists(dir_path)
    assert os.path.exists(dir_path)

# Тест для read_json_file
def test_read_json_file(tmpdir):
    test_file = tmpdir.join("test.json")
    test_file.write('{"key": "value"}')
    result = read_json_file(str(test_file), 'utf-8')
    assert result == {"key": "value"}

    empty_file = tmpdir.join("empty.json")
    empty_file.write("")
    result = read_json_file(str(empty_file), 'utf-8')
    assert result == []

# Тест для read_json_file_or_false
def test_read_json_file_or_false(tmpdir):
    test_file = tmpdir.join("test.json")
    test_file.write('{"key": "value"}')
    result = read_json_file_or_false(str(test_file), 'utf-8')
    assert result == {"key": "value"}

    non_existent_file = tmpdir.join("non_existent.json")
    result = read_json_file_or_false(str(non_existent_file), 'utf-8')
    assert result is False

# Тест для write_json_file
def test_write_json_file(tmpdir):
    test_file = tmpdir.join("test.json")
    data = {"key": "value"}
    write_json_file(data, str(test_file), 'utf-8')
    with open(test_file, 'r', encoding='utf-8') as file:
        result = json.load(file)
    assert result == data

# Тест для append_to_json_file
def test_append_to_json_file(tmpdir):
    test_file = tmpdir.join("test.json")
    initial_data = [{"key": "initial_value"}]
    write_json_file(initial_data, str(test_file), 'utf-8')
    
    new_data = {"key": "new_value"}
    append_to_json_file(new_data, str(test_file), 'utf-8')
    
    with open(test_file, 'r', encoding='utf-8') as file:
        result = json.load(file)
    
    assert result == initial_data + [new_data]

# Тест для add_transaction
def test_add_transaction(tmpdir):
    test_file = tmpdir.join("transactions.json")
    add_transaction(100, str(test_file), 'utf-8')
    
    with open(test_file, 'r', encoding='utf-8') as file:
        transactions = json.load(file)
    
    assert len(transactions) == 1
    assert transactions[0]['amount'] == 100

# Тест для get_latest_balance
def test_get_latest_balance(tmpdir):
    test_file = tmpdir.join("transactions.json")
    transactions = [
        {"amount": 100, "datetime": "2023-01-01 10:00:00.000"},
        {"amount": 200, "datetime": "2023-01-02 10:00:00.000"}
    ]
    write_json_file(transactions, str(test_file), 'utf-8')
    
    latest_balance = get_latest_balance(str(test_file), 'utf-8')
    assert latest_balance == 200

# Тест для add_buying_history
def test_add_buying_history(tmpdir):
    test_file = tmpdir.join("expence_history.json")
    add_buying_history("item", 50, str(test_file), 'utf-8')
    
    with open(test_file, 'r', encoding='utf-8') as file:
        history = json.load(file)
    
    assert len(history) == 1
    # assert history[0]['name'] == "item"
    # assert history[0]['cost'] == 50
    assert history[-1]['name'] == "item"
    assert history[-1]['cost'] == 50


# Тест для get_bying_history
def test_get_bying_history(tmpdir):
    test_file = tmpdir.join("expence_history.json")
    history = [
        {"name": "item1", "cost": 50},
        {"name": "item2", "cost": 100}
    ]
    write_json_file(history, str(test_file), 'utf-8')
    
    result = get_bying_history(str(test_file), 'utf-8')
    assert result == history

# Тест для to_buy
def test_to_buy(tmpdir):
    transaction_file = tmpdir.join("transactions.json")
    expence_file = tmpdir.join("expence_history.json")

    # Сначала добавляем начальный баланс
    add_transaction(200, str(transaction_file), 'utf-8')

    # Проверяем, что баланс корректный
    latest_balance = get_latest_balance(str(transaction_file), 'utf-8')
    assert latest_balance == 200

    # Пробуем купить предмет
    success = to_buy("item", 150, str(expence_file), str(transaction_file), 'utf-8')
    assert success is True

    # Проверяем баланс после покупки
    latest_balance = get_latest_balance(str(transaction_file), 'utf-8')
    assert latest_balance == 50

    # Проверяем историю покупок
    history = get_bying_history(str(expence_file), 'utf-8')
    assert len(history) == 1
    assert history[0]['name'] == "item"
    assert history[0]['cost'] == 150



# def test_to_buy(tmpdir):
#     transaction_file = tmpdir.join("transactions.json")
#     expence_file = tmpdir.join("expence_history.json")
    
#     # Сначала добавляем начальный баланс
#     add_transaction(200, str(transaction_file), 'utf-8')
    
#     # Пробуем купить предмет
#     success = to_buy("item", 150, str(expence_file), str(transaction_file), 'utf-8')
#     assert success is True
    
#     # Проверяем баланс
#     latest_balance = get_latest_balance(str(transaction_file), 'utf-8')
#     assert latest_balance == 50
    
#     # Проверяем историю покупок
#     history = get_bying_history(str(expence_file), 'utf-8')
#     assert len(history) == 1
#     assert history[0]['name'] == "item"
#     assert history[0]['cost'] == 150


# тесстирование функций программы "мой счет"
# from utils.acc_func import account_info, display_history

# # Фикстура для начального состояния счета и истории покупок
# @pytest.fixture
# def initial_state():
#     return {
#         'account_money': 0,
#         'buying_history': []
#     }

# # Тест для функции account_info
# def test_account_info(initial_state):
#     account_money = initial_state['account_money']
#     assert account_info(account_money) == account_money

# # Тест для функции display_history  с использованием захвата стандартного вывода capsys
# def test_display_history_empty(capsys):
#     buying_history = []
#     display_history(buying_history)
#     captured = capsys.readouterr()
#     assert 'История покупок пуста.' in captured.out

# def test_display_history_non_empty(capsys):
#     buying_history = [('еда', 50)]
#     display_history(buying_history)
#     captured = capsys.readouterr()
#     assert '1. еда - 50' in captured.out


