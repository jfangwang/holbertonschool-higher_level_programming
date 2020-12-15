#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = 0
    for benny in my_list:
        if (count == idx):
            my_list[idx] = element
            return my_list
        count += 1
    return my_list
