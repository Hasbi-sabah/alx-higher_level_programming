#!/usr/bin/python3
"""
This module creates a class Square.
"""


class Square:
    """
    A class named Square.
    """
    def __init__(self, size=0):
        """
        Initializes a new private instance of the Square class.
        And raises TypeError andValueError

        Args:
            _Square__size (int): Size of square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """
        Calculates area of square.
        """
        return self._Square__size ** 2
