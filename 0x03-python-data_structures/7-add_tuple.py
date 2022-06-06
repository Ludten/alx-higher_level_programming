#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) < 2:
        a = list(tuple_a)
        a.append(0)
        tuple_a = tuple(a)
    elif len(tuple_a) > 2:
        a = list(tuple_a)
        tuple_a = tuple(a[:2])

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) < 2:
        b = list(tuple_b)
        b.append(0)
        tuple_b = tuple(b)
    elif len(tuple_a) > 2:
        b = list(tuple_b)
        tuple_b = tuple(b[:2])

    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
