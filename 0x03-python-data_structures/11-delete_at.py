#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    count = 0
    for benny in my_list:
        if (count == idx):
            del my_list[idx]
            return my_list
        count += 1
    return my_list
