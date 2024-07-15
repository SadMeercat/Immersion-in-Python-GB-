# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def get_file_extension(files_name):
    splited_filenames = []

    for i in files_name:
        splited_filenames.append(os.path.splitext(i))
    return splited_filenames

def rename_files(filespath: str, filename: str, start_ext: str, fin_ext: str, start_range: int, end_range: int, num_digits: int = 3) -> None:
    all_files = os.listdir(filespath)

    number = 0
    for file_name, file_ext in get_file_extension(all_files):
        if start_ext in file_ext:
            final_file_name = ''
            final_file_name += file_name[start_range:end_range]
            final_file_name += filename
            final_file_name += f'{number:0{num_digits}}'
            number += 1
            if '.' in fin_ext:
                final_file_name += fin_ext
            else:
                final_file_name += f'.{fin_ext}'

            filepath = os.path.join(filespath,file_name + file_ext)

            with open(filepath, 'r') as file:
                content = file.readlines()

            os.remove(filepath)

            with open(os.path.join(filespath, final_file_name), 'w') as file:
                file.writelines(content)

def reset_files(path:str):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    file_names = ['file1.txt', 'file2.md', 'file3.py', 'file4.html', 'file5.csv', 'file6.txt', 'file7.txt']

    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        with open(file_path, 'w') as file:
            file.write('rnd content')
    

    

if __name__ == '__main__':
    path = 'G:/_Disk/gb.ru/Разработчик - DataEngineer/Погружение в Python/HW7/files/'

    reset_files(path)

    rename_files(filespath=path, filename='wasd', start_ext='txt', fin_ext='html', start_range=0, end_range=9)