# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

if __name__ == '__main__':
    flag = True
    while(flag):
        try:
            number = int(input('Введите число от 1 до 100 тыс.: '))
        except:
            print('Некорректный ввод')
            continue

        if number > 0 and number <100000:
            flag = False
            is_simple = True
            for i in range(2,number):
                if number % i == 0:
                    is_simple = False
                    break 
            if is_simple:
                print('Число является простым')
            else:
                print('Число является составным')
        else:
            print('Некорректный ввод')