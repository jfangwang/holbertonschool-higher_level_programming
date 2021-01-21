#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    with open(filename, 'r+', encoding='utf-8') as file:
        content = file.readlines()
        lc = 0
        while lc < len(content):
            if search_string in content[lc]:
                lc += 1
                content.insert(lc, new_string)
            lc += 1
        file.seek(0)
        for line in content:
            file.write(line)
