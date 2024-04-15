#!/usr/bin/python3

"""A class that inherit from a list"""


class MyList(list):
    """
        This class inherit from list.
        Attribute:
        Methods:
        Returns: Prints the list ij ascending order
    """
    def print_sorted(self):
        """ Method that prints a list in ascending order """
        sorted_list = sorted(self)
        print(sorted_list)
