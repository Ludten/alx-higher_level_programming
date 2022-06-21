#!/usr/bin/python3
"""
A module for calculating the area and circumference
of a circle.
"""
import math


class MagicClass:
    """
    A class used to represent A circle

    Args:
        radius (int): radius of the circle

    Attributes:
        radius (int): where the radius is stored
    """

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        """
        Calculates the area of the circle

        Returns:
            The area
        """
        return ((self.radius ** 2) * math.pi)

    def circumference(self):
        """
        Calculates the circumference of the square

        Returns:
            The circumference
        """
        return (2 * math.pi * self.radius)
