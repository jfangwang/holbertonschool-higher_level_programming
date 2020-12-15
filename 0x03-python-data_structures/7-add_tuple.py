#!/bin/bash
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check(tuple_a)
    tuple_b = check(tuple_b)
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))


def check(tup=()):
    if len(tup) == 1:
        tup = (tup[0], 0)
    elif len(tup) == 0:
        tup = (0, 0)
    elif len(tup) > 2:
        tup = (tup[0], tup[1])

    return tup
