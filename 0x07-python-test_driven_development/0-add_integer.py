#!/usr/bin/python3
"""
Module to add 2 ints
"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.

    Args:
        a : Argument
        b : Argument
            (default is 98)

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)
    return a + b
