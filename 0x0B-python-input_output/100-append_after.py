#!/usr/bin/python3
"""
Module for the function append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str)
        search_string (str)
        new_string (str)
    """
    with open(filename, "r") as f:
        text = f.readlines()
    for num, line in enumerate(text, 1):
        if search_string in line:
            text[num:num] = new_string
    with open(filename, "w") as f:
        f.writelines(text)
