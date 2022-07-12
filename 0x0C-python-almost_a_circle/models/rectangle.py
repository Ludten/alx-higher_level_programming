#!/usr/bin/python3
"""
Module defining a rectangle model
"""
from models.base import Base


class Rectangle(Base):
    """
    Class representing a rectangle

    Args:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x coordinate
        y (int): y coordinate

    Attributes:
        width (int)
        height (int)
        x (int)
        y (int)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get and set the width of the rectangle

        Args:
            value (int): width of rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
            ValueError: if value is less than or equal zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Get and set the x coord

        Args:
            value (int): x coord

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Get and set the y coord

        Args:
            value (int): y coord

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            The area
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle
        """
        print('{}'.format('\n' * self.y), end='')
        for i in range(self.height):
            print('{}{}'.format(' ' * self.x, '#' * self.width))

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width,
            self.height)

    def update(self, *args, **kwargs):
        """
        update the attributes of the rectangle
        """
        if ((args != [] or args != ()) and len(args) > 0):
            for i, j in zip(self.__dict__, args):
                self.__dict__[i] = j
        else:
            for i, j in kwargs.items():
                if hasattr(self, i):
                    setattr(self, i, j)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the
        rectangle class

        Returns:
            dict
        """
        recdict = self.__dict__.copy()
        recdict['width'] = recdict.pop('_Rectangle__width')
        recdict['height'] = recdict.pop('_Rectangle__height')
        recdict['x'] = recdict.pop('_Rectangle__x')
        recdict['y'] = recdict.pop('_Rectangle__y')
        return recdict
