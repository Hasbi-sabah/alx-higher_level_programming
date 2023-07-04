#!/usr/bin/python3
"""
Module to print names
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints My name is <first name> <last name>

    Args:
        first_name : Argument
        last_name : Argument
            (default is '')

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
