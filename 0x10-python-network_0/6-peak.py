#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ find_peak Time complexity: O(log(n))"""
    """
    list_of_integers: An array of numbers that could contain a peak number
    """
    middle = int(len(list_of_integers) / 2)
    # print(str(list_of_integers) + " middle is: " + str(middle))
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            print(list_of_integers[1])
            return list_of_integers[1]
    """Prospects array has to be bigger than 3"""

    if list_of_integers[middle + 1] > list_of_integers[middle]:
        new_arr = []
        new_arr = list_of_integers[middle + 1:len(list_of_integers)]
        return find_peak(new_arr)
    if list_of_integers[middle - 1] > list_of_integers[middle]:
        new_arr = []
        new_arr = list_of_integers[middle - 1:0]
        return find_peak(new_arr)
    if (list_of_integers[middle] >= list_of_integers[middle + 1] and
       list_of_integers[middle] >= list_of_integers[middle + 1]):
        return list_of_integers[middle]
