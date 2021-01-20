#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    openfile = open(filename)
    for a in openfile:
        print(a, end='')
    openfile.close()
