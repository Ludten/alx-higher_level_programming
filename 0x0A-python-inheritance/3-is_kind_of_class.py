#!/usr/bin/python3
"""
A module that checks object instance
"""


def is_kind_of_class(obj, a_class):
    """
    function to check if obj is of instance a_class

    Args:
        obj (object): object being checked
        a_class (object): classes

    Returns:
        True or False
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
