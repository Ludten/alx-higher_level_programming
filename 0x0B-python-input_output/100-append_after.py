#!/usr/bin/python3
"""
A module of file search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts new_string into a file
    after each line containing search_string

    Args:
        filename (str): filename
        search_string (str): string to append after
        new_string (str): string to be added to file
    """
    out_txt = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            if search_string in line:
                line = line + new_string
            out_txt += line

    with open(filename, 'w', encoding="utf-8") as out_f:
        out_f.write(out_txt)
