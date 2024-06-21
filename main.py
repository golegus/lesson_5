import os
import sys
from utils.fs_func import new_dir,rm_dir,copy_item,print_items,list_dir,list_files,list_folders,come_to_dir
from utils.acc_func import account_upgrade,display_history,buying



def account():
    account_money = 0
    buying_history = []

    while True:
        print('='*10)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('='*10)
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account_money = account_upgrade(account_money)
        elif choice == '2':
            account_money, buying_history = buying(account_money, buying_history)
        elif choice == '3':
            display_history(buying_history)
        elif choice == '4':
            print('Выход из программы.')
            break
        else:
            print('Неверный пункт меню. Попробуйте снова.')


def main():
    while True:
        print('='*20)
        print("1 - создать папку;")
        print("2 - удалить (файл/папку);")
        print("3 - копировать (файл/папку);")
        print("4 - просмотр содержимого рабочей директории;")
        print("5 - посмотреть только папки;")
        print("6 - посмотреть только файлы;")
        print("7 - просмотр информации об операционной системе;")
        print("8 - создатель программы;")
        print("9 - играть в викторину;")
        print("10 - мой банковский счет;")
        print("11 - смена рабочей директории (*необязательный пункт);")
        print("12 - выход.")
        print('='*20)
        choice = input('Выберите пункт меню: ')
        print('='*20)
        if   choice == '1':
            new_dir()
        elif choice == '2':
            rm_dir()
        elif choice == '3':
            copy_item()
        elif choice == '4':
            print_items("Содержимое текущей папки:",list_dir())
            print ('='*20)
        elif choice == '5':
            print_items("Папки в текущем каталоге:",list_folders())
            print ('='*20)    
        elif choice == '6':
            print_items("Файлы в текущем каталоге:",list_files())
            print ('='*20)
        elif choice == '7':
            print('My OS is', sys.platform, '(', os.name, ')')
        elif choice == '8':
            print ('*'*24)
            print('* СОЗДАТЕЛЬ!: О.В.Гущин *')
            print ('*'*24)
        elif choice == '9':
            pass
        elif choice == '10':
            account()
            pass
        elif choice == '11':
            come_to_dir()
        elif choice == '12':
            print('Выход из программы.')
            break
        else:
            print('Неверный пункт меню. Попробуйте снова.')
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()