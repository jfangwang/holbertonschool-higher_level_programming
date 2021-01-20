#!/usr/bin/python3
"""task 12"""


def pascal_triangle(n):
    """pascal"""
    row = 0
    bucket1 = 0
    triangle = []
    rowArr = []
    count = 0

    if n <= 0:
        return triangle

    triangle = [[1]]

    if n == 1:
        return triangle

    for a in range(1, n):
        """n is greater than 2"""
        count = 0
        rowArr = []
        for index in range(0, a + 1):
            rowArr.append(count)
            print(count)
            count += 1
        triangle.append(rowArr)
    print(triangle)
    return triangle
