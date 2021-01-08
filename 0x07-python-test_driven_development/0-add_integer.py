#!/usr/bin/python3
"""Function Add Int """
import doctest


def add_integer(a, b=98):
    try:
        a = int(a)
    except:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except:
        raise TypeError("a must be an integer")
    return a + b
    doctest.testfile("tests/0-add_integer.txt")
