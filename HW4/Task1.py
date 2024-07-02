# Напишите функцию для транспонирования матрицы

def matrix_transporition(matrix):
    row = []
    result_matrix = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result_matrix.append(row)
        row = []
    return result_matrix

if __name__ == '__main__':
    my_matrix1 =[
        [1, 2, 3],
        [4, 5, 6]
    ]
    my_matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    my_matrix3 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    for i in matrix_transporition(my_matrix1):
        print(i)
    print()

    for i in matrix_transporition(my_matrix2):
        print(i)
    print()

    for i in matrix_transporition(my_matrix3):
        print(i)