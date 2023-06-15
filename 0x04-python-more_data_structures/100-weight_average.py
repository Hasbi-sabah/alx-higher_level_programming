#!/usr/bin/python3
# This is a function that returns the weighted average
# of all integers tuple (<score>, <weight>)

def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0
    dev = 0
    for n in my_list:
        result += n[0] * n[1]
        dev += n[1]
    result /= dev
    return result
