#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    willy = []
    for i in my_list:
        if i % 2 == 0:
            willy.append(True)
        else:
            willy.append(False)
    return willy
