#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0):
        """
        init square

        Args:
            size: the size
        """
        self.__size = size

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area

        Returns:
            Returns the area
        """
        return self.__size ** 2

    def __lt__(self, value):
        """Less Than"""
        return self.size < value.size

    def __le__(self, value):
        """Less Than Equal"""
        return self.size <= value.size

    def __eq__(self, value):
        """Equal"""
        return self.size == value.size

    def __ne__(self, value):
        """Not Equal"""
        return self.size != value.size

    def __gt__(self, value):
        """Greater Than"""
        return self.size > value.size

    def __ge__(self, value):
        """Greater Than Equal"""
        return self.size >= value.size
