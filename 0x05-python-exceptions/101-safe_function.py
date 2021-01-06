#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as a:
        sys.stderr.write("Exception: " + str(a) + '\n')
    return None
