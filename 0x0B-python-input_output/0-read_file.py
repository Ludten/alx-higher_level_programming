#!/usr/bin/python3
"""
A module that reads a file
"""


def read_file(filename=""):
    """
    A function that opens and reads a file

    Args:
        filename (str)
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
