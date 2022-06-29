#!/usr/bin/python3
"""
A module with a function that prints name with
strings
"""


def say_my_name(first_name, last_name=""):
    """
    print name

    Args:
        first_name (string)
        last_name (string)

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
