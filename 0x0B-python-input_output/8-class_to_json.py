#!/usr/bin/python3
"""
A module that gets the dictionary description of objects
"""


def class_to_json(obj):
    """
    A function that returns the dictionary description of
    objects

    Args:
        obj (type)

    Returns:
        dict (any)
    """
    return (obj.__dict__)
