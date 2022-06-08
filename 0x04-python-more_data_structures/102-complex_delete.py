#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = a_dictionary.values()
    for val in values:
        if val == value:
            for i, j in a_dictionary.items():
                if j == value:
                    del a_dictionary[i]
            return a_dictionary
    return a_dictionary
