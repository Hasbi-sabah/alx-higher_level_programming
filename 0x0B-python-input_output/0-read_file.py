#!/usr/bin/python3
"""
Module for the function read_file()
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): default ""
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
