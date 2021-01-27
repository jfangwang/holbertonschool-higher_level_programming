#!/usr/bin/python3
"""base"""
import json


class Base:
    """base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        l = []
        fn = cls.__name__ + ".json"

        if list_objs:
            for a in list_objs:
                l.append(a.to_dictionary())
        with open(fn, 'w') as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            willy = cls(1, 1)
            cls.update(willy, **dictionary)
            return willy
        elif cls.__name__ == "Square":
            willy = cls(1)
            cls.update(willy, **dictionary)
            return willy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        l = []
        fn = cls.__name__ + ".json"
        try:
            with open(fn) as f:
                p = cls.from_json_string(f.read())
            for a in p:
                l.append(cls.create(**a))
        except:
            pass
        return l
