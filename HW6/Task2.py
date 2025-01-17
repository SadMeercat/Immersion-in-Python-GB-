# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from Package import check_queens_mod as cq
from random import randint

def generate_queens():
    success = 0
    while success < 4:
        queens = []
        for i in range(8):
            queens.append((randint(0,8), randint(0, 8)))
        if cq.check_queens(queens):
            success += 1
            print(f'Успех №{success}\r\n{queens}')

if __name__ == '__main__':
    queens = [
        (1, 1),
        (2, 5),
        (3, 8),
        (4, 6),
        (5, 3),
        (6, 7),
        (7, 2),
        (8, 4)
    ]

    print(cq.check_queens(queens))