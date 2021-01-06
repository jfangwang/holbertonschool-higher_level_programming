#!/usr/bin/python3
import dis

class MagicClass:




    def __init__(self, radius):
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('readius must be a number')
        self.__radius = radius
    
    dis.dis(__init__)
    def area():
        return self.__radius ** 2 * math.pi

    dis.dis(area)
    def circumference():
        return 2 * math.pi * self.__radius
    dis.dis(circumference) 
