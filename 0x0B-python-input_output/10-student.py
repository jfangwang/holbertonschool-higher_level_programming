#!/usr/bin/python3
"""class student"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve a dict"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            """there is a list of attrs"""
            dic = {}
            for a in attrs:
                if type(a) is str:
                    try:
                        dic[a] = self.__dict__[a]
                    except:
                        pass
            return dic
