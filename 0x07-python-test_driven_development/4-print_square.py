#!/usr/bin/python3
"""Print Square"""


def print_square(size):
    """Print Square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        for b in range(size):
            print('#', end='')
        if b == size - 1:
            print()
