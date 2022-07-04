#!/usr/bin/python3
"""
A module that checks object type
"""


def is_same_class(obj, a_class):
    """
    function to check if obj is of type a_class

    Args:
        obj (object): object being checked
        a_class (object): classes

    Returns:
        True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
