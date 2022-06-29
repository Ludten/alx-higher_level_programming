#!/usr/bin/python3
"""
A module with a function for adding two
integers
"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a (int)
        b (int)

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        sum of integers
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
