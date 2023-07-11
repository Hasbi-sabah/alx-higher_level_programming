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
    with open(filename, "w") as f:
        for line in text:
            f.write(line)
            if search_string in line:
                f.write(new_string)
