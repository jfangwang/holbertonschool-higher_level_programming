#!/usr/bin/python3
"""matrix"""


def matrix_mul(m_a, m_b):
    """matrix_multiplied"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    err = "m_a should contain only integers or floats"
    num = ""
    matrix = m_a

    for a in range(len(matrix)):
        if type(matrix[a]) is not list:
            raise TypeError(err)
        if len(matrix[0]) != len(matrix[a]):
            raise TypeError("each row of m_a must be of the same size")
        for b in range(len(matrix[a])):
            num = matrix[a][b]
            if type(num) is not int and type(num) is not float:
                raise TypeError(err)
    err = "m_b should contain only integers or floats"
    matrix = m_b

    for a in range(len(matrix)):
        if type(matrix[a]) is not list:
            raise TypeError(err)
        if len(matrix[0]) != len(matrix[a]):
            raise TypeError("each row of m_b must be of the same size")
        for b in range(len(matrix[a])):
            num = matrix[a][b]
            if type(num) is not int and type(num) is not float:
                raise TypeError(err)
    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = []
    for a in range(len(m_a)):
        row = []
        for b in range(len(m_a[0])):
            num = 0
            for c in range(len(m_b[0])):
                num += m_a[a][c] * m_b[c][b]
            row.append(num)
        new_matrix.append(row)
    return new_matrix
