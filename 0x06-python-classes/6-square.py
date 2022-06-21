#!/usr/bin/python3
"""
A module for working with squares.
"""


class Square:
    """
    A class used to represent A square

    Args:
        size (int): length and width of square
        position (tuple): displacement of sqaure

    Attributes:
        size (int): where the size is stored
        position (tuple): where the position is stored
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Get and set position of square

        Args:
        value (tuple): displacement of sqaure

        Raises:
            TypeError: if an integer in tuple is not positive
        """
        return self.__position

    @position.setter
    def position(self, value):
        is_invalid_value = True
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            The area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square
        """
        if self.__size == 0:
            print('')
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print('')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                for j in range(self.size):
                    print('#', end='')
                print('')
