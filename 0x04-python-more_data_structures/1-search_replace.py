#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    count = 0
    for a in new:
            if a == search:
                new[count] = replace
            count += 1
    return new
