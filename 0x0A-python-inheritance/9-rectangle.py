#!/usr/bin/python3
"""task 8"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __str__(self):
        """returns dimensions"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
