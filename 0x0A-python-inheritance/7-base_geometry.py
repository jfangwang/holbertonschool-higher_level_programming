#!/usr/bin/python3
"""task 7"""


class BaseGeometry():
    """Base Geometry Class"""
    def area(self):
        """exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
