#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """read file"""
    openfile = open(filename, encoding='utf-8')

    for a in openfile:
        print(a, end='')
    openfile.close()
