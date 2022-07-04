#!/usr/bin/python3
"""
A module for working with geometry & rectangles.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a square

    Args:
        size (int): length & width of square

    Attributes:
        width (int): where the size is stored
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
