#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size=None, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, size):
        """setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """str"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update"""
        index = 0
        attrs = ["id", "size", "x", "y"]
        if len(args) != 0:
            for a in args:
                setattr(self, attrs[index], args[index])
                index += 1
        else:
            for k, v in kwargs.items():
                for a in range(len(attrs)):
                    if k == attrs[a]:
                        setattr(self, attrs[a], v)

    def to_dictionary(self):
        """to dictionary"""
        return {'x': self.x, 'y': self.y, 'id': self.y, 'size': self.size}
