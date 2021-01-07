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
        if len(new_matrix[0]) != len(new_matrix[a]):
            raise TypeError("Each row of the matrix must have the same size")
        for b in range(len(new_matrix[a])):
            if type(new_matrix[a][b]) is not int and type(new_matrix[a][b]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[a][b] = round(new_matrix[a][b] / div, 2)
    return new_matrix
