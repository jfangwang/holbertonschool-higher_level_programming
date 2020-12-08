#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ""
    pos = 0
    for i in str:
        if (pos != n):
            newstring += i
        pos += 1
    return (newstring)
