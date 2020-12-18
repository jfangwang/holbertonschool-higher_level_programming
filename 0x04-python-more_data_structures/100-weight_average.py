#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score, weight, points, total = 0, 0, 0, 0
    for tuple in my_list:
        score = tuple[0]
        weight = tuple[1]
        points += score * weight
        total += weight
    return points / total
