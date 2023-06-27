#!/usr/bin/python3
"""
This module creates an empty class Square.
"""


class Square:
    """
    An empty class named Square.
    """
    def __init__(self, size=0):
        """
        Initializes a new private instance of the Square class.

        Args:
            size (int): Size of square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square.
        """
        return self.size ** 2

    def __int__(self):
        return self.area()
