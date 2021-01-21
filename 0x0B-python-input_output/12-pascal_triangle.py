#!/usr/bin/python3
"""task 12"""


def pascal_triangle(n):
    """pascal"""
    rowArr = []
    triangle = []
    num1 = 0
    num2 = 0

    if n <= 0:
        return triangle
    triangle = [[1]]
    if n == 1:
        return triangle

    for a in range(2, n + 1):
        """row"""
        rowArr = []
        num1 = 0
        num2 = 0
        for b in range(0, a):
            """col"""
            """prints the index of the previous row"""
            if b < a - 1:
                print(triangle[a - 2][b])
                num1 = triangle[a - 2][b]
                rowArr.append(num1 + num2)
                num2 = num1
            if b == a - 1:
                rowArr.append(1)
        triangle.append(rowArr)
    return triangle
