#!/usr/bin/python3
"""
A module that checks object subclass
"""


def inherits_from(obj, a_class):
    """
    function to check if obj is of subclass a_class

    Args:
        obj (object): object being checked
        a_class (object): classes

    Returns:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
