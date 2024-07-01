# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

def gdc(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    greatest_common_divisor = gdc(numerator, denominator)

    simplified_numerator = numerator // greatest_common_divisor
    simplified_denominator = denominator // greatest_common_divisor

    return simplified_numerator, simplified_denominator


if __name__ == '__main__':
    while True:
        try:
            fraction1_str = input('Введите первую дробь в формате a/b: ')
            fraction1 =list(map(int, fraction1_str.split('/')))
            fraction2_str = input('Введите вторую дробь в формате a/b: ')
            fraction2 = list(map(int, fraction2_str.split('/')))
        except:
            print('Некорректный ввод')
            continue
        if len(fraction1) == 2 and len(fraction2) == 2:
            numerator = fraction1[0] * fraction2[1] + fraction2[0] * fraction1[1]
            denominator = fraction1[1]*fraction2[1]

            numerator, denominator = simplify_fraction(numerator, denominator)
            sum = f'{numerator}/{denominator}'
            print(f'Сумма дробей: {sum}')
            print(f'Контрольная сумма дробей: {Fraction(fraction1_str) + Fraction(fraction2_str)}')

            numerator = fraction1[0] * fraction2[0]
            denominator = fraction1[1] * fraction2[1]

            numerator, denominator = simplify_fraction(numerator, denominator)
            mul = f'{numerator}/{denominator}'
            print(f'Произведение дробей: {mul}')
            print(f'Контрольное произведение дробей: {Fraction(fraction1_str) * Fraction(fraction2_str)}')
            break
        else:
            print('Некорректный ввод')