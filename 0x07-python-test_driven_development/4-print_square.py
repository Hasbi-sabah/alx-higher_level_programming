#!/usr/bin/python3
"""
Module to print a square
"""


def print_square(size):
    """
    A function that prints a square with the character #.

    Args:
        size : Argument

    """
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    elif type(size) is float:
        size = int(size)
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
