#!/usr/bin/python3
def best_score(a_dictionary):
    high = 0
    name = ""
    if not a_dictionary:
        return None
    for a, b in a_dictionary.items():
        if b > high:
            name = a
    return name
