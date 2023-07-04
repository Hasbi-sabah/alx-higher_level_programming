#!/usr/bin/python3
"""
Module for class LockedClass
"""


class LockedClass:
    """
    class LockedClass
    """

    def __setattr__(self, attr, name):
        """
        Sets only first_name attr

        Args:
            self : Argument
            attr : Argument
            name : Argument

        """
        if attr != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute {}".format(attr)
            )
        self.__dict__[attr] = name
