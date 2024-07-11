from _pytest.compat import LEGACY_PATH
from utils.fs_func import list_dir, list_folders, list_files, save_dir_to_file
import pytest
import os


@pytest.fixture
def list_dir_fixt():
    items=[]
    for item in os.listdir():
        items.append(item)
    return items

@pytest.fixture
def list_files_fixt(list_dir_fixt: list):
    files=[]
    current_directory = os.getcwd()
    for item in list_dir_fixt:
         if os.path.isfile(os.path.join(current_directory, item)):
             files.append(item)
    return files

@pytest.fixture
def list_folders_fixt(list_dir_fixt: list):
    folders=[]
    current_directory = os.getcwd()
    for item in list_dir_fixt:
        if os.path.isdir(os.path.join(current_directory, item)):
            folders.append(item)
    return folders

def test_list_dir(list_dir_fixt: list):
    items=list_dir()
    assert items==list_dir_fixt

def test_list_files(list_files_fixt: list):
    items=list_files()
    assert items==list_files_fixt

def test_list_folders(list_folders_fixt: list):
    items=list_folders()
    assert items==list_folders_fixt

def test_save_dir_to_file(tmpdir,list_files_fixt: list, list_folders_fixt: list):
    files=", ".join(list_files_fixt)
    folders=", ".join(list_folders_fixt)
    file_content=f"files: {files}\nfolders: {folders}\n"
    test_file = tmpdir.join("listdir.txt")  
    save_dir_to_file(test_file)
    with open(test_file, "r", encoding='utf-8') as f:
        assert file_content==f.read()
    