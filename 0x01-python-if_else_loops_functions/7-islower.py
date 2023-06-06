#!/usr/bin/python3
# This is a function that checks for lowercase character.

def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    return False
