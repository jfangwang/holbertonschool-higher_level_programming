#!/usr/bin/python3
"""task 1"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    with open(filename, encoding='utf-8') as b:
        content = b.read()
        return len(content)
