#!/usr/bin/python3
"""
A module for working with squares.
"""


class Square:
    """
    A class used to represent A square

    Args:
        size (int): length and width of square

    Attributes:
        size (int): where the size is stored
    """

    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
