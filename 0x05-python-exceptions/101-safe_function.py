#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as exc:
        res = None
        sys.stderr.write("Exception: {}\n".format(exc))

    return res
