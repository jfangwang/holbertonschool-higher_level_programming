#!/usr/bin/python3
"""task 3"""


def append_write(filename="", text=""):
    """append write"""
    with open(filename, mode='a', encoding='utf-8') as a:
        return a.write(text)
