#!/usr/bin/python3

"""A class that inherit from a list"""


class MyList(list):
    def print_sorted(self):
        """ Method """
        sorted_list = sorted(self)
        print(sorted_list)
