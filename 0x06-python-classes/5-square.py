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

    """size

    Getter, Retrieves the size value

    Returns:
        int: the value

    """
    @property
    def size(self):
        return self.__size

    """size

    Setter, Sets the size value

    Args:
        value (int): sets the value

    """

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """area method

    The area method returns the current square area

    Rasies:
        TypeError: If size is not an int
        ValueError: If size < 0

    Returns:
        int: returns the sqaure area

    """
    def area(self):
        return self.__size * self.__size
    """my_print

    Prints in stdout the square with # char

    """
    def my_print(self):
        length = int(self.__size)

        if length == 0:
            print()
            return None
        for a in range(length):
            for b in range(length):
                print('#', end='')
                if b == length - 1:
                    print()
            if a == length:
                return None
