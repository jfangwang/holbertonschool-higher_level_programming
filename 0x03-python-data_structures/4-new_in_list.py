#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = 0
    blist = []
    for benny in my_list:
        blist.append(my_list[count])
        if (count == idx):
            blist[count] = element
        count += 1
    return blist
