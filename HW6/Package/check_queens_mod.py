__all__ = ['check_queens']

def check_queens(positions: list) -> bool:
    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()
    
    for row, col in positions:
        if row in rows or col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False
        rows.add(row)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
    
    return True

if __name__ == '__main__':
    queens1 = [
        (1, 1),
        (2, 5),
        (3, 8),
        (4, 6),
        (5, 3),
        (6, 7),
        (7, 2),
        (8, 4)
    ]
    queens2 = [
        (1, 1),
        (2, 2),
        (3, 8),
        (4, 6),
        (5, 3),
        (6, 7),
        (7, 2),
        (8, 4)
    ]

    print(check_queens(queens1))
    print(check_queens(queens2))