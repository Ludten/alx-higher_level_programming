#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        for k in a_dictionary.copy():
            if a_dictionary[k] == value:
                del a_dictionary[k]
        return a_dictionary
    return a_dictionary
