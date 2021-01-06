#!/usr/bin/python3
"""Square Class"""


class Square:
    """This is a class"""
    def __init__(self, size=0, position=(0, 0)):
        """method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """sizes getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """sizes setter function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """positions getter function"""
        return self.__position

    @position.setter
    def position(self, value):
        """positions setter function"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area method"""
        return self.__size ** 2

    def my_print(self):
        """my_print prints out the square"""
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__position[1]):
                print("")
            for a in range(self.__size):
                for b in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print('#', end="")
                print("")

    def __str__(self):
        """Returns String"""
        sqr = ""
        if self.__size == 0:
            sqr += "\n"
            return sqr
        else:
            for a in range(self.__position[1]):
                sqr += "\n"
            for a in range(self.__size):
                for b in range(self.__position[0]):
                    sqr += " "
                for b in range(self.__size):
                    sqr += "#"
                if a < self.__size - 1:
                    sqr += "\n"
        return sqr
