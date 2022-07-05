#!/usr/bin/python3
"""
A module that write into a file
"""


def write_file(filename="", text=""):
    """
    A function that opens and writes into a file

    Args:
        filename (str)

    Returns:
        number of characters written into file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
