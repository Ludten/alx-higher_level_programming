#!/usr/bin/python3
"""
A module that add attributes to an object
"""


def add_attribute(obj, name, value):
    """
    A function that adds an attribute to an object

    Args:
        obj (object)
        name (str)
        value (any)
    """
    if hasattr(obj, "__weakref__") is True:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
