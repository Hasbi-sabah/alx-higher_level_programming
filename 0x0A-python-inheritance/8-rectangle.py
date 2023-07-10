#!/usr/bin/python3
"""
Module for the class BaseGeometry
"""


class BaseGeometry:
    """
    Class with public instance methods: area and integer_validator
    """

    def area(self):
        """
        Raises Exception with msg 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates value

        Args:
            name (str)
            value (int)
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


"""
Module for the class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height, private and positive ints

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
