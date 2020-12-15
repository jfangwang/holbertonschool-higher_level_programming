#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    for benny in my_list:
        if (count == idx):
            return my_list[idx]
        count += 1
    return None
