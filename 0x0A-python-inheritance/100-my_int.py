#!/usr/bin/python3
"""
Module with a class that inherits int object
"""


class MyInt(int):
    """
    A class that inherit's int object
    """

    def __eq__(self, __x):
        return super().__ne__(__x)

    def __ne__(self, __x):
        return super().__eq__(__x)
