#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ find_peak Time complexity: O(log(n))"""
    if list_of_integers == []:
        return None
    return(find(list_of_integers, 0, len(list_of_integers)))


def find(num_arr, low, high):
    """num_arr: An array of numbers"""
    size = high - low
    middle = low + int(size/2)

    if (num_arr[middle] >= num_arr[middle + 1] and
       num_arr[middle] >= num_arr[middle + 1]):
        return num_arr[middle]
    elif num_arr[middle + 1] > num_arr[middle]:
        return find(num_arr, middle + 1, high - 1)
    else:
        return find(num_arr, 0, middle - 1)
