#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ find_peak Time complexity: O(log(n))"""
    if list_of_integers == []:
        return None
    return(find(list_of_integers, 0, len(list_of_integers) - 1))


def find(num_arr, low, high):
    """num_arr: An array of numbers"""
    size = high - low
    middle = low + int(size/2)
    if low == high or ((num_arr[middle - 1] < num_arr[middle]) and (num_arr[middle + 1] < num_arr[middle])):
        return num_arr[middle]
    elif num_arr[middle + 1] > num_arr[middle]:
        return find(num_arr, middle + 1, high)
    else:
        return find(num_arr, low, middle - 1)
