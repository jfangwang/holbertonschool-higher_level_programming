#!/usr/bin/python3
def no_c(my_string):
    word = ""
    for benny in my_string:
        if benny == 'c' or benny == 'C':
            continue
        else:
            word += benny
    return word
