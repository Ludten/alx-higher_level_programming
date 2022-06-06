#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    co_list = my_list.copy()
    if (idx < 0 or idx >= len(my_list)):
        return co_list
    co_list[idx] = element
    return co_list
