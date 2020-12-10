#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    if len(argv) == 1:
        print("0")
    else:
        for willy in range(1, len(argv)):
            total += int(argv[willy])
        print("{:d}".format(total))
