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

    def __init__(self, size):
        self.__size = size
