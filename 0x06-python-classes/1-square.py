#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """ This class represent a square"""

# We then define a constructor
    def __init__(self, size):
        """ Initislize a new square

        Argument:
            size(integer): The size of the new square

        """
        self.__size = size
