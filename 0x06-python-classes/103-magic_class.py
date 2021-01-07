#!/usr/bin/python3
"""Magic Class"""
import math
import dis

class MagicClass:
    """ Magic Class"""
    def __init__(self, radius=0):
        """__init__"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """circumference"""
        return (2 * math.pi * self.__radius)
    dis.dis(__init__)
    dis.dis(area)
    dis.dis(circumference)
