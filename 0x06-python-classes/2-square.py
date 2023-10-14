#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """ This class represent a square"""

# We then define a constructor
    def __init__(self, size=0):
        """ Initislize a new square

        Argument:
            size(integer): The size of the new square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
