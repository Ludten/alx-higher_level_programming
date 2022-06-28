#!/usr/bin/python3
"""
A module that showcases locked class
instance attribute
"""


class LockedClass:
    """
    A class showing instance attribute
    locking
    """
    __slots__ = ['first_name']

    def __init__(self):
        pass
