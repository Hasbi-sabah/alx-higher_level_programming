#!/usr/bin/python3
# This is a function that returns a new
# dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    new_dic = {x: y * 2 for x, y in a_dictionary.items()}
    return new_dic
