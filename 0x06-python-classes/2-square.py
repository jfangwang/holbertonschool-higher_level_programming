#!/usr/bin/python3
"""Square Class"""


class Square:

    """__init__ method

    The __init__ method intializes a size of the square

    Note:
        This is annoying and I am gonna have to learn this and I
        understand why this is necessay.

    Attributes:
        size (int): A private value defining the square

    Rasies:
        TypeError: If size is not an int
        ValueError: If size < 0


    """

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
