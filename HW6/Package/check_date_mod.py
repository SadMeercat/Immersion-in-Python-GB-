__all__ = ['check_date']

def _is_leap(year)->bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def check_date(date:str) -> bool:
    try:
        day, month, year = map(int, date.split('.'))

        if year < 1 or month < 1 or month > 12 or day < 1:
            return False
        
        days_in_month = [31, 29 if _is_leap(year) else 28, 31, 30, 31, 31, 30, 31, 30, 31]

        if day > days_in_month[month - 1]:
            return False
        
        return True
        
    except (ValueError, IndexError):
        return False
    
if __name__ == '__main__':
    date1 = "11.02.9999"  # Високосный год
    date2 = "29.02.2023"  # Невисокосный год
    date3 = "31.04.2024"  # Некорректная дата
    date4 = "30.04.2024"  # Корректная дата

    print(check_date(date1))  # True
    print(check_date(date2))  # False
    print(check_date(date3))  # False
    print(check_date(date4))  # True