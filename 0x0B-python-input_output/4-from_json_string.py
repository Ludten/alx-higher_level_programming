#!/usr/bin/python3
"""
A module that converts JSON strings to python objects
"""

import json


def from_json_string(my_str):
    """
    A function that converts json strings to python
    objects

    Args:
        my_str (str)

    Returns:
        python object (any)
    """
    return (json.loads(my_str))
