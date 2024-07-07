import os, sys, json
from utils.fs_func import new_dir,rm_dir,copy_item,print_items,list_dir,list_files,list_folders,come_to_dir
from utils.acc_func import get_latest_balance,add_transaction,to_buy, get_bying_history

 
def account_info():
    amount=get_latest_balance()
    print(f'На Вашем счету {amount}')
    return amount

def account_upgrade():
    amount=account_info()
    up_val = int(input('Введите сумму, на которую желаете пополнить счет: '))
    amount += up_val
    add_transaction(amount)
    print(f'Счет пополнен на {up_val}. На Вашем счету теперь {amount}')
    return amount

def display_history():
    buying_history=get_bying_history()
    print('*'*20)
    if not buying_history:
        print('История покупок пуста.')
    else:
        for entry in buying_history:
#            amount = entry.get("amount")
#            datetime = entry.get("datetime")
            print(f'{entry.get("name")} - {entry.get("cost")}')
#            print(*entry.values())
#        for idx, (name, val) in enumerate(buying_history, start=1):
#            print(f'{idx}. {name} - {cost}')
    print('*'*20)

def account():
    while True:
        print('='*20)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('='*20)
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account_upgrade()
        elif choice == '2':
            account_money=account_info()
            if account_money == 0:
                print('На счету нет денег. Вы ничего не можете купить.')
            else:
                name = input('Введите название: ')
                cost = int(input('Введите цену: '))
#                order = (name,cost)
                if to_buy(name,cost):
                    print(f'Вы купили {name} на сумму {cost}')
                    print('Поздравляем с покупкой!')             
                else:
                    print('*'*32)
                    print(f'* Недостаточно денег на счету! *')
                    print('*'*32)
                print('='*20)
                account_info()
        elif choice == '3':
            display_history()
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