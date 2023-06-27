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
        And raises TypeError and ValueError

        Args:
            _Square__size (int): Size of square.
        """
        self._Square__size = size

    @property
    def size(self):
        """
        Getter for the class Square
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter for the class Square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        """
        Calculates area of square.
        """
        return self._Square__size ** 2

    def my_print(self):
        """
        Prints square.
        """
        if self._Square__size == 0:
            print()
        for i in range(self._Square__size):
            for j in range(self._Square__size):
                print("#", end='')
            print()
