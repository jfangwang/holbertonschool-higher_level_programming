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

    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        self.__size = value
    """position

    Getter, Retrieves the size value

    Returns:
        int: the value

    """
    @property
    def position(self):
        return self.__position

    """position

    Setter, Sets the size value

    Args:
        value (int): sets the value

    """

    @position.setter
    def size(self, value):
        if type(value) != tuple or value[0] < 0 or value[1] < 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or type(value[0]) != int or type(value[1] != 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        for a in range(self.__position[1]):
            print()
        if length == 0:
            print()
            for c in range(self.__position[0]):
                print(' ', end='')
            return None
        for a in range(length):
            for c in range(self.__position[0]):
                print(' ', end='')
            for b in range(length):
                print('#', end='')
                if b == length - 1:
                    print()
            if a == length:
                return None
