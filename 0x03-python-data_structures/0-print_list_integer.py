#!/usr/bin/python3
""" A function that prints all integer of a list"""


def print_list_integer(my_list=[]):
    for integer in range(len(my_list)):
        print("{:d}".format(my_list[integer]))
