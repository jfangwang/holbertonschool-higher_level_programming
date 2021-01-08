#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    err = "matrix must be a matrix (list of lists) of integers/floats"
    num = ""

    for a in range(len(matrix)):
        if type(matrix[a]) is not list:
            raise TypeError(err)
        if len(matrix[0]) != len(matrix[a]):
            raise TypeError("Each row of the matrix must have the same size")
        for b in range(len(matrix[a])):
            num = matrix[a][b]
            if type(num) is not int and type(num) is not float:
                raise TypeError(err)
    return (list(map(lambda row:
                 list(map(lambda x: round(x / div, 2), row)), matrix)))
