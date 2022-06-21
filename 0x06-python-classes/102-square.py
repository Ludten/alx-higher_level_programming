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
        self.__size = size

    @property
    def size(self):
        """
        Get and set size of square

        Args:
        value (int): length and width of square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            The area
        """
        return self.__size * self.__size

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size == other.__size

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size != other.__size

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size < other.__size

    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size <= other.__size

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size > other.__size

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size >= other.__size


s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
