#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if len(my_list_1) != len(my_list_2):
        raise IndexError
    output = []
    count = 0

    try:
        for a in my_list_1:
            output[count] = my_list_1[count] / my_list_2[count]
            count += 1
    except IndexError:
        print("out of range")
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    else:
        print(output)
