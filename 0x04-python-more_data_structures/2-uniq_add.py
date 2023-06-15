#!/usr/bin/python3
# This is a function that adds all unique integers in a list.

def uniq_add(my_list=[]):
    new_list = set(my_list)
    summ = sum(int(i) for i in new_list)
    return summ
