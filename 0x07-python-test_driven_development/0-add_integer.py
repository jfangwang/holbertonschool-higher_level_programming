#!/usr/bin/python3
"""Function Add Int """


def add_integer(a, b=98):
    """add_int"""
    try:
        a = int(a)
    except:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except:
        raise TypeError("b must be an integer")
    return a + b
