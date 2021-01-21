#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding='utf-8') as openfile:
        for a in openfile:
            print(a, end='')
