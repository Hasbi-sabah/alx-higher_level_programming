#!/usr/bin/python3
"""
Defines class MagicClass
"""
import math


class MagicClass:
    """
    Class MagicClass
    """
    def __init__(self, radius=0):
        """
        Initialize circle
        """
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self._MagicClass__radius = radius
        return

    def area(self):
        """
        Calculate circle area
        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculate circle circumference
        """
        return (math.pi * 2) * self._MagicClass__radius
