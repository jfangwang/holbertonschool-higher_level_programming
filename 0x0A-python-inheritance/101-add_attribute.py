#!/usr/bin/python3
"""add attribute"""


def add_attribute(obj, name, value):
    """add strribute"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
