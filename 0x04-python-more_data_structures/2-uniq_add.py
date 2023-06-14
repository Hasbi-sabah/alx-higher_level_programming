#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    summ = sum(int(i) for i in new_list)
    return summ
