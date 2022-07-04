#!/usr/bin/python3
"""
Module with a class that inherits list object
"""


class MyList(list):
    """
    A class that inherit's list object
    """

    def print_sorted(self):
        """
        print sorted MyList
        """
        slist = self[:]
        slist.sort()
        print(slist)
