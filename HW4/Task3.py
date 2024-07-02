
def take_tax(balance):
    if balance >= 5000000:
        balance = balance - balance*0.1
    return balance

def accural_interest(actions_counter, balance):
    if actions_counter % 3 == 0:
        balance = add_balance(balance, balance*0.03)
    return balance

def add_balance(balance, amount):
    balance = take_tax(balance)
    balance += amount
    return balance

def take_balance(balance, amount):
    balance = take_tax(balance)
    if balance < amount:
        print('Недостаточно средств')
    else:
        tmp_tax = amount * 0.15
        if tmp_tax < 30:
            tmp_tax = 30
        elif tmp_tax > 600:
            tmp_tax = 600
        balance -= amount + tmp_tax
    return balance


if __name__ == '__main__':
    balance = 0
    action_counter = 0
    history = []
    while(True):
        print(f'Баланс: {balance}')
        print('Выберете действие: ')
        print('1. Внести')
        print('2. Снять')
        print('3. История операций')
        print('4. Выйти')
        choice = input('Действие: ')

        if choice == '1':
            try:
                amount = int(input('Введите сумму пополнения: '))
            except:
                print('Неверный ввод')
                continue

            if amount%50 != 0:
                print('Некорректное пополнение')
            else:
                balance = add_balance(balance, amount)
                history.append(['Пополнение', str(amount)])
                action_counter += 1
                balance = accural_interest(action_counter, balance)

        elif choice == '2':
            try:
                amount = int(input('Введите сумму снятия: '))
            except:
                print('Неверный ввод')
                continue

            if amount%50 != 0:
                print('Некорректное снятие')
            else:
                balance = take_balance(balance, amount)
                history.append(['Снятие', str(amount)])
                action_counter += 1
                balance = accural_interest(action_counter, balance)
        elif choice == '3':
            for i in history:
                print(':'.join(i))
        elif choice == '4':
            break
        else:
            print('Неправильный ввод')
        print()
        
