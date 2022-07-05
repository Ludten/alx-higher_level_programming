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
    with open(filename, 'r', encoding="utf-8") as in_f, \
            open('out.txt', 'w', encoding="utf-8") as out_f:
        for line in in_f:
            if search_string in line:
                print(line)
                line = line + new_string
                out_f.write(line)
            else:
                out_f.write(line)

    with open('out.txt', 'r', encoding="utf-8") as out_f, \
            open(filename, 'w', encoding="utf-8") as in_f:
        new_str = out_f.read()
        in_f.write(new_str)
