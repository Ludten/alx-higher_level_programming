#!/usr/bin/python3
"""
A module that appends into a file
"""


def append_write(filename="", text=""):
    """
    A function that opens and appends into a file

    Args:
        filename (str)

    Returns:
        number of characters written into file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
