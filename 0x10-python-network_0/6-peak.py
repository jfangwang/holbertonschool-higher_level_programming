#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ find_peak Time complexity: O(log(n))"""
    # print("\nnew list\n")
    if list_of_integers == []:
        return None
    else:
        return(find(list_of_integers, 0, len(list_of_integers)))


def find(num_arr, low, high):
    """
    num_arr: An array of numbers that could contain a peak number
    """
    # print(num_arr)
    size = high - low
    middle = low + int(size/2)
    # print(low, high)
    # print(str(num_arr) + " middle is: " + str(middle))
    if high == low == middle:
        return num_arr[middle]
    if high - low == 1:
        if num_arr[high] > num_arr[low]:
            return num_arr[high]
        else:
            return num_arr[low]
    """num_arr has to be bigger than 3"""
    if (num_arr[middle] >= num_arr[middle + 1] and
       num_arr[middle] >= num_arr[middle + 1]):
        return num_arr[middle]
    if num_arr[middle + 1] > num_arr[middle]:
        return find(num_arr, middle + 1, high - 1)
    if num_arr[middle - 1] > num_arr[middle]:
        return find(num_arr, 0, middle - 1)
