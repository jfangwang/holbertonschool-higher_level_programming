#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (IndexError, TypeError, ValueError) as a:
        sys.stderr.write("Exception: " + str(a) + '\n')
        return False
