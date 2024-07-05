from utils.fs_func import list_dir, list_folders, list_files
import pytest
import os


@pytest.fixture
def list_dir_fixt():
    items=[]
    for item in os.listdir():
        items.append(item)
    return items

@pytest.fixture
def list_files_fixt(list_dir_fixt):
    files=[]
    current_directory = os.getcwd()
    for item in list_dir_fixt:
         if os.path.isfile(os.path.join(current_directory, item)):
             files.append(item)
    return files

@pytest.fixture
def list_folders_fixt(list_dir_fixt):
    folders=[]
    current_directory = os.getcwd()
    for item in list_dir_fixt:
        if os.path.isdir(os.path.join(current_directory, item)):
            folders.append(item)
    return folders

def test_list_dir(list_dir_fixt):
    items=list_dir()
    assert items==list_dir_fixt

def test_list_files(list_files_fixt):
    items=list_files()
    assert items==list_files_fixt

def test_list_folders(list_folders_fixt):
    items=list_folders()
    assert items==list_folders_fixt


# тесстирование функций программы "мой счет"
from utils.acc_func import account_info, display_history

# Фикстура для начального состояния счета и истории покупок
@pytest.fixture
def initial_state():
    return {
        'account_money': 0,
        'buying_history': []
    }

# Тест для функции account_info
def test_account_info(initial_state):
    account_money = initial_state['account_money']
    assert account_info(account_money) == account_money

# Тест для функции display_history  с использованием захвата стандартного вывода capsys
def test_display_history_empty(capsys):
    buying_history = []
    display_history(buying_history)
    captured = capsys.readouterr()
    assert 'История покупок пуста.' in captured.out

def test_display_history_non_empty(capsys):
    buying_history = [('еда', 50)]
    display_history(buying_history)
    captured = capsys.readouterr()
    assert '1. еда - 50' in captured.out


