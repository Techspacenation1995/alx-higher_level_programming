#!/usr/bin/python3
""" A program that prints all integers of a list, in reverse order """
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        print("{:d}".format(my_list[len(my_list) - 1]))
        print_reversed_list_integer(my_list[:-1])
