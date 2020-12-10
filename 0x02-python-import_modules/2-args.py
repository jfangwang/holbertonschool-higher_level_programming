#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for a in range(1, len(argv)):
            print("{:d}: {:s}".format(a, argv[a]))
