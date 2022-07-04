#!/usr/bin/python3
"""
Module to get all available attributes and methods
of an object
"""


def lookup(obj):
    """
    Function that returns a list of available
    attributes and methods of an obj

    Args:
        obj (object)

    Returns:
        list
    """
    obj_met = [method_name for method_name in dir(
        obj) if callable(getattr(obj, method_name))]
    return obj_met
