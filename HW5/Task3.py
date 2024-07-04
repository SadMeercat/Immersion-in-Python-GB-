# Создайте функцию генератор чисел Фибоначчи

def fib_generator(n):
    result = []
    for i in range(n + 1):
        if len(result) < 2:
            result.append(i)
        else:
            result.append(result[i-1] + result[i-2])
    return result

if __name__ == '__main__':
    while True:
        try:
            n = int(input('Введите значение n: '))
        except:
            print('Неверное значение n')
            print()
            continue
        
        result = fib_generator(n)
        print(result)
        break