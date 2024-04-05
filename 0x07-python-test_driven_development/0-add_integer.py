#!/usr/bin/python3

""" A function that adds two integers """


def add_integer(a, b=98):
    """
    Args: a, b which is either an integer or float
    Return: an integer( addition of a and b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)
    return (a + b)
