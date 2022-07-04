#!/usr/bin/python3
"""
A module working with geometry
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
        if isinstance(value, (int)) is not True:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
