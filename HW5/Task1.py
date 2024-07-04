# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

if __name__ == '__main__':
    while True:
        file = input('Введите путь до файла: ')

        if os.path.exists(file):
            basename, extension = os.path.splitext(file)
            result = (file, os.path.basename(file), extension)
            print(result)
            break
        else:
            print('Неверный путь к файлу')
            print()