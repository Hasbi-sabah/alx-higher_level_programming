#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attr, name):
        """
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
