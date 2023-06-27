#!/usr/bin/python3
"""
This module creates an empty class Square.
"""


class Square:
    """
    An empty class named Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new private instance of the Square class.

        Args:
            _Square__size (int): Size of square.
        """
        self._Square__size = size
        self._Square__position = position

    @property
    def size(self):
        """
        Getter of size for the class Square
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter of size for the class Square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        """
        Getter of position for the class Square
        """
        return self._Square__position

    @position.setter
    def position(self, value):
        """
        Setter of position for the class Square
        """
        if type(value) is not tuple or len(value) != 2 \
                or type(value[0]) is not int \
                or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

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
            return
        for i in range(self._Square__position[1]):
            print()
        for i in range(self._Square__size):
            for k in range(self._Square__position[0]):
                print(' ', end='')
            for j in range(self._Square__size):
                print("#", end='')
            print()
