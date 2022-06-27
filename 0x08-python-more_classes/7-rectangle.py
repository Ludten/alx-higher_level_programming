#!/usr/bin/python3
"""
A module for working with rectangles.
"""


class Rectangle:
    """
    An empty class used to represent A rectangle

    Args:
        width (int): width of rectangle
        height (int): height of rectangle

    Attributes:
        width (int): where the width is being stored
        height (int): where the height is being stored
        number_of_instances (int): number of instances
        print_symbol (string): rectangle symbol to print
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Get and set the width of the rectangle

        Args:
            value (int): width of rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get and set the height of the rectangle

        Args:
            value (int): height of rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            The area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            The perimeter
        """
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        return class
        """
        rec = ""
        if (self.__height == 0 or self.__width == 0):
            return rec
        else:
            for j in range(self.__height):
                for x in range(self.__width):
                    rec += str(self.print_symbol)
                rec += '\n'
            return rec[:-1]

    def __repr__(self):
        """
        return class instance representation
        """
        reprec = "Rectangle" + \
            "(" + str(self.width) + "," + str(self.height) + ")"
        return reprec

    def __del__(self):
        """
        delete class instance representation
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
