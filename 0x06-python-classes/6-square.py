#!/usr/bin/python3
"""Square Class"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """size getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter function"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter function"""
        return self.__position

    @position.setter
    def size(self, value):
        """position setter function"""
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area method"""
        return self.__size * self.__size

    def my_print(self):
        """my_print prints out the square"""
        if self.__size == 0:
            print("")
            return None
        for a in range(self.__position[1]):
            print("")
        for a in range(self.__size):
            for b in range(self.__position[0]):
                print(" ", end='')
            for b in range(self.__size):
                print('#', end='')
            print("")
