#!/usr/bin/python3
# This is a function that creates a copy of the string,
# removing the character at the position n.

def remove_char_at(str, n):
    cpy = ""
    for i in range(0, len(str)):
        if i != n:
            cpy += str[i]
    return cpy
