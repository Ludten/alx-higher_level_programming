#!/usr/bin/python3
"""
Module defining a square model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing a square

    Args:
        size (int): height & width of square
        x (int): x coordinate
        y (int): y coordinate

    Attributes:
        width (int)
        height (int)
        x (int)
        y (int)
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Get and set the size of the square

        Args:
            value (int): size of square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal zero
        """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """
        update the attributes of the square
        """
        if ((args != [] or args != ()) and len(args) > 0):
            sqdict = self.__dict__.copy()
            del sqdict['_Rectangle__height']
            for i, j in zip(sqdict, args):
                self.__dict__[i] = j
        else:
            for i, j in kwargs.items():
                if i == 'size':
                    i = "width"
                    if hasattr(self, i):
                        setattr(self, i, j)
                    i = "height"
                    if hasattr(self, i):
                        setattr(self, i, j)
                elif hasattr(self, i):
                    setattr(self, i, j)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the
        rectangle class

        Returns:
            dict
        """
        sqdict = self.__dict__.copy()
        sqdict['size'] = sqdict.pop('_Rectangle__width')
        del sqdict['_Rectangle__height']
        sqdict['x'] = sqdict.pop('_Rectangle__x')
        sqdict['y'] = sqdict.pop('_Rectangle__y')
        return sqdict
