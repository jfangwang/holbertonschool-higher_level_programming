#!/usr/bin/python3
"""task 8"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """init"""
        Rectangle.__init__(self, size, size)
        self.__size = size
