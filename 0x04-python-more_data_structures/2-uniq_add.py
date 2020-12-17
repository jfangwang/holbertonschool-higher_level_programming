#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    new = []
    for a in my_list:
        if a not in new:
            new.append(a)
    return sum(new)
