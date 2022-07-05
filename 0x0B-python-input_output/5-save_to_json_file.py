#!/usr/bin/python3
"""
A module that converts python objects to JSON and
saves them as text files
"""

import json


def save_to_json_file(my_obj, filename):
    """
    A function that converts objects to their json
    representation and saves them as text files

    Args:
        my_obj (any)
        filename (str)
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
