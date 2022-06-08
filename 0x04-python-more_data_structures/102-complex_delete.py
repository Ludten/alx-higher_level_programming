#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        new_dict = {k: v for k, v in a_dictionary.items() if v != value}
        return new_dict
    return a_dictionary
