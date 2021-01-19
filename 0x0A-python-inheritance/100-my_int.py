#!/usr/bin/python3
"""my int rebel"""


class MyInt(int):
    """int"""
    def __eq__(self, other):
        """ == will be !="""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ != will be =="""
        return int.__eq__(self, other)
