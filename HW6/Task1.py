# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import HW6.Package.check_date_mod as cd
from sys import argv

if __name__ == '__main__':
    try:
        date = argv[1]
        print('Дата существует' if cd.check_date(date) else 'Даты не сущевствует')
    except IndexError:
        print('Нет параметров')