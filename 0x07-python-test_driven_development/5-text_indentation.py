#!/usr/bin/python3
def text_indentation(text):
    """indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new = ""
    a = 0

    while a < len(text):
        new += text[a]
        if text[a] == '.' or text[a] == '?' or text[a] == ':':
            print(new)
            print()
            new = ""
            if text[a + 1] == ' ':
                a += 1
        a += 1
