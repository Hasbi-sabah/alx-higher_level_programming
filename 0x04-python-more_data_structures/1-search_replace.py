#!/usr/bin/python3
# This is a function that replaces all
# occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    new_list = [i if i is not search else replace for i in my_list]
    return new_list
