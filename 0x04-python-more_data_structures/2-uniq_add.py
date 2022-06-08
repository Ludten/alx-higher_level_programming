#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    res = 0
    for i in set_list:
        res += i
    return res
