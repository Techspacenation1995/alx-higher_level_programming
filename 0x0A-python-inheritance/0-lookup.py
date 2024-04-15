#!/usr/bin/python3

def lookup(obj):
    """
    Returns the List of available attributes and methos of an object.

    Parameters:
        obj (object): The object to inspect

    Returns:
        list: A list containing that availabale attributes
        and method of the object
    """
    return dir(obj)
