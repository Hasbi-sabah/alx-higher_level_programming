#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    black_list = []
    for x, y in a_dictionary.items():
        if value is y:
            black_list.append(x)
    for i in reversed(black_list):
            del a_dictionary[i]
    return a_dictionary
