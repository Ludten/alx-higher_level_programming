#!/usr/bin/python3
"""
A module with a function that prints a square
"""


def print_square(size):
    """
    Prints the square

    Args:
        size (int)

    Raises:
        TypeError: if size is not an integer or a float
        with negative value
        ValueError: if size is a negative number
    """
    if isinstance(size, (int, float)) is not True:
        raise TypeError("size must be an integer")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print('')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print('')
