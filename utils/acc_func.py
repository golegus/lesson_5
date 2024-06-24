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

def account_info(account_money):
    print(f'На Вашем счету {account_money}')
    return account_money

def account_upgrade(account_money):
    account_info(account_money)
    up_val = int(input('Введите сумму, на которую желаете пополнить счет: '))
    account_money += up_val
    print(f'Счет пополнен на {up_val}. На Вашем счету теперь {account_money}')
    return account_money

def buying(account_money, buying_history):
    account_info(account_money)
    if account_money == 0:
        print('На счету нет денег. Вы ничего не можете купить.')
        return account_money, buying_history
    else:
        cost = int(input(f'Введите сумму покупки: '))
        if cost > account_money:
            print('Сумма покупки превышает количество денег на счету.')
            return account_money, buying_history
        buying_name = input('Введите наименование покупки: ')
        account_money -= cost
        buying_history.append((buying_name, cost))
        print(f'Покупка {buying_name} на сумму {cost} завершена.')
        return account_money, buying_history

def display_history(buying_history):
    print('*'*10)
    if not buying_history:
        print('История покупок пуста.')
    else:
        for idx, (name, val) in enumerate(buying_history, start=1):
            print(f'{idx}. {name} - {val}')
    print('*'*10)

