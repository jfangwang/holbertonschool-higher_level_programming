#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ find_peak """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    if len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    """ list has to have 3 or more numbers """
    index = 1
    pre = 0
    nex = 0
    cur = 0
    peak = None
    while index < len(list_of_integers) - 1:
        pre = list_of_integers[index - 1]
        nex = list_of_integers[index + 1]
        cur = list_of_integers[index]
        if ((pre <= cur) and (nex <= cur)):
            if peak is None:
                peak = cur
            if cur > peak:
                peak = cur
        index += 1
    return str(peak)
