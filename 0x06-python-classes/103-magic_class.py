#!/usr/bin/python3
import dis
import math


class MagicClass:


    def __init__(self, radius):
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('readius must be a number')
        self.__radius = radius


    def area(self):
        return self.__radius ** 2 * math.pi


    def circumference(self):
        return 2 * math.pi * self.__radius
    dis.dis(__init__)
    dis.dis(area)
    dis.dis(circumference)
