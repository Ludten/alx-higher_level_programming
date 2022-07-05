#!/usr/bin/python3
"""
A module that converts python objects to JSON
"""

import json


def to_json_string(my_obj):
    """
    A function that converts objects to their
    json representation

    Args:
        my_obj (any)

    Returns:
        json representation (str)
    """
    return (json.dumps(my_obj))
