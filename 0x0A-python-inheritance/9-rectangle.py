#!/usr/bin/python3
"""
A module for working with geometry & rectangles.
"""


class BaseGeometry:
    """
    A class used to represent geometry
    """

    def area(self):
        """
        calculate area of polygon
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check the integer value
        """
        if isinstance(name, str) is not True:
            raise Exception("'name' must be a string")
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate area of polygon
        """
        return self.__width * self.__height

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
