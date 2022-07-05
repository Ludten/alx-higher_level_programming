#!/usr/bin/python3
"""
A module that reads JSON files and converts python objects
"""

import json


def load_from_json_file(filename):
    """
    A function that reads json files and converts their string
    to python objects

    Args:
        filename (str)

    Returns:
        python object (any)
    """
    with open(filename, 'r', encoding="utf-8") as f:
        s_json = f.read()
        return (json.loads(s_json))
