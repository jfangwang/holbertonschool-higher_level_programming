#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = matrix

    for a in range(len(new_matrix)):
        if type(new_matrix[a]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for b in range(len(new_matrix[a])):
            if type(new_matrix[a][b]) is not float and type(new_matrix[a][b]) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[a][b] = round(new_matrix[a][b] / div, 2)
    return new_matrix
