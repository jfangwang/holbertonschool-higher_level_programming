#!/usr/bin/python3
"""Rectangle"""
from models.base import Base


class Rectangle(Base):
    """rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area"""
        return self.__height * self.__width

    def display(self):
        """display"""
        for x in range(self.__y):
            print()
        for row in range(self.__height):
            for y in range(self.__x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.
                                                       y, self.width, self.
                                                       height)

    def update(self, *args, **kwargs):
        """update"""
        if len(args) != 0:
            index = 0
            attrs = ["id", "width", "height", "x", "y"]
            for a in args:
                setattr(self, attrs[index], args[index])
                index += 1
        else:
            for a, b in kwargs.items():
                setattr(self, a, b)

    def to_dictionary(self):
        """to dictionary"""
        dict = {}
        index = 0
        attrs = ["id", "width", "height", "x", "y"]
        for a in attrs:
            dict[index] = getattr(self, a)
        return dict
