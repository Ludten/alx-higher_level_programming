#!/usr/bin/python3
"""
A module that defines a Student class
"""


class Student:
    """
    A class that represents a student

    Args:
        first_name (str)
        last_name (str)
        age (int)

    Attributes:
        first_name (str)
        last_name (str)
        age (int)
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dictionary representation of Student
        class

        Returns:
            __dict__ (any)
        """
        if attrs is not None:
            new_dict = {}
            for keys in attrs:
                for (k, v) in self.__dict__.items():
                    if k == keys:
                        new_dict[keys] = self.__dict__[k]
            return new_dict
        else:
            return self.__dict__
