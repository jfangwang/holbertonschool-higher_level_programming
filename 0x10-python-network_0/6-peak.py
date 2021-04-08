#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ find_peak Time complexity: O(log(n))"""
    return(find(list_of_integers, 0, len(list_of_integers) - 1))
def find(prospects_arr, low, high):
    """
    prospects_arr: An array of numbers that could contain a peak number
    """
    middle = int(low/high)
    # print(str(prospects_arr) + " middle is: " + str(middle))
    if len(prospects_arr) == 0:
        return None
    if len(prospects_arr) == 1:
        return prospects_arr[0]
    if len(prospects_arr) == 2:
        if prospects_arr[0] > prospects_arr[1]:
            return prospects_arr[0]
        else:
            return prospects_arr[1]
    """prospects_arr has to be bigger than 3"""
    if (prospects_arr[middle] >= prospects_arr[middle + 1] and
       prospects_arr[middle] >= prospects_arr[middle + 1]):
        return prospects_arr[middle]
    if prospects_arr[middle + 1] > prospects_arr[middle]:
        new_arr = []
        new_arr = prospects_arr[middle + 1:high]
        return find(new_arr, middle + 1, high)
    if prospects_arr[middle - 1] > prospects_arr[middle]:
        new_arr = []
        new_arr = prospects_arr[middle - 1:0]
        return find(new_arr, 0, middle)
