# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

if __name__ == '__main__':
    print('Загадываю число...')
    rnd_number = randint(0, 1000)

    attempt = 0

    while attempt < 10:
        try:
            inpt = int(input(f'Введите число (попытка {attempt + 1}): '))
        except:
            print('Некорректный ввод')
            continue

        if rnd_number > inpt:
            print('Загаданное число больше')
        elif rnd_number < inpt:
            print('Загаданное число меньше')
        else:
            print('Вы победили!')
            break
        attempt += 1
    else:
        print(f'Загаданное число: {rnd_number}')
