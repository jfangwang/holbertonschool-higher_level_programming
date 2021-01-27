#!/usr/bin/python3
"""This is Rectangle File."""
from models.base import Base


class Rectangle(Base):
    """This is a rectangle"""
    def __init__(self, width=None, height=None, x=0, y=0, id=None):
        """An init function to start"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter function"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter function"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter function"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter function"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter function"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area function"""
        return self.__height * self.__width

    def display(self):
        """display function"""
        for x in range(self.__y):
            print()
        for row in range(self.__height):
            for y in range(self.__x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """A str function that is long"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """An update function"""
        index = 0
        attrs = ["id", "width", "height", "x", "y"]

        if len(args) != 0:
            for a in args:
                setattr(self, attrs[index], args[index])
                index += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A to dictionary function"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
