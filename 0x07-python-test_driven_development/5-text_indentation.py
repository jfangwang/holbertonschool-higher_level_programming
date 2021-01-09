#!/usr/bin/python3
"""indentation"""


def text_indentation(text):
    """indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new = ""
    a = 0
    p = 0

    while a < len(text):
        new += text[a]
        if text[a] == '.' or text[a] == '?' or text[a] == ':':
            print(new)
            print()
            new = ""
            p = 1
            if a + 1 < len(text) and text[a + 1] == ' ':
                a += 1
        a += 1
    if p == 0:
        print(new)
