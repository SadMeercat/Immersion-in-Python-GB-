# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

if __name__ == '__main__':
    flag = True
    
    letters = {10: 'a',
               11: 'b',
               12: 'c',
               13: 'd',
               14: 'e',
               15: 'f'}

    while flag:
        try:
            number = int(input('Введите число: '))
            tmp_number = number
            flag = False
        except:
            print('Некорректный ввод')
            continue
        result = ''
        
        while tmp_number > 16:
            div = tmp_number % 16

            if div >= 10:
                result += letters[div]
            else:
                result += str(div)
            tmp_number = tmp_number // 16

        else:
            if tmp_number >= 10:
                result += letters[tmp_number]
            else:
                result += str(tmp_number)
    else:
        print(f'Результат: 0x{''.join(reversed(result))}')
        print(f'Контрольное значение: {hex(number)}')
