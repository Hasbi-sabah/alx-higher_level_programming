#!/usr/bin/python3
"""
Module fot the function print_all
"""


def print_all(size, codes):
    """
    Function that prints all, duh!

    Args:
        size (int): size of file
        codes (dict): codes dictionnary
    """
    print("File size: {}".format(size))
    for key in codes:
        if codes[key] != 0:
            print("{}: {}".format(key, codes[key]))


"""
Module for the main portion
"""

big_size = 0
big_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
while True:
    size = 0
    codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    for i in range(10):
        try:
            line = input()
        except KeyboardInterrupt:
            print_all(big_size, big_codes)
            raise KeyboardInterrupt()
        lines = line.split()
        size += int(lines[-1])
        big_size += int(lines[-1])
        for key in codes:
            if int(key) == int(lines[-2]):
                codes[key] += 1
                big_codes[key] += 1
    print_all(size, codes)
