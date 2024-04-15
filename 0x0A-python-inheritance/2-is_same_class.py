#!/usr/bin/python3
""" A function that determines if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class

    Args:

        obj(any): The pbject to check.
        a_class (type): The class to match the type of the object

    Returns:
        True: If obj is exactly an instance.
        False: Otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
