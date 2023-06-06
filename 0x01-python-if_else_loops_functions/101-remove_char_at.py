#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    for i in len(str):
        if i != n:
            cpy.append(str[i])
    return cpy
