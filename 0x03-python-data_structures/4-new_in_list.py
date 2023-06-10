#!/usr/bin/python3
# This is a function that replaces an element in a list
# at a specific position without modifying the original list (like in C).

def new_in_list(my_list, idx, element):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(element if i == idx else my_list[i])
    return new_list
