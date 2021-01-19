#!/usr/bin/python3
"""my int rebel"""


class MyInt(int):
    """int"""
    def __eq__(self, other):
        """ == will be !="""
        return False

    def __ne__(self, other):
        """ != will be =="""
        return True
