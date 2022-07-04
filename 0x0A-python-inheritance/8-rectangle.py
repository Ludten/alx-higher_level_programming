#!/usr/bin/python3
"""
A module for working with geometry & rectangles.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a rectangle

    Args:
        width (int): width of rectangle
        height (int): height of rectangle

    Attributes:
        width (int): where the width is being stored
        height (int): where the height is being stored
    """

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
