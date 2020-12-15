#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for benny in matrix:
            count = 0
            for adam in benny:
                    if count == len(benny) - 1:
                        print("{:d}".format(adam))
                    else:
                        print("{:d}".format(adam), end=' ')
                    count += 1
        print()
