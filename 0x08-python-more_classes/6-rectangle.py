#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Reactangle Class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__"""
        output = ""
        if self.__width == 0 or self.__height == 0:
            return output
        for a in range(self.__height):
            for b in range(self.__width):
                output += str(self.print_symbol)
            if a < self.__height - 1:
                output += '\n'
        return output

    def __repr__(self):
        """__repr__"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """__del__"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
