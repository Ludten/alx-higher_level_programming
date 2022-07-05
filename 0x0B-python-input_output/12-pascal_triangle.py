#!/usr/bin/python3
"""
A module on pascal triangle
"""


def pascal_triangle(n):
    """
    A function computing pascal triangle into
    p_tri of p_tris

    Args:
        n (int)

    Returns:
        p_tri
    """
    p_tri = []
    if n <= 0:
        return p_tri
    else:
        for i in range(n):
            p_tri.append([])
            p_tri[i].append(1)
            for j in range(1, i):
                p_tri[i].append(p_tri[i - 1][j - 1] + p_tri[i - 1][j])
            if(i != 0):
                p_tri[i].append(1)
    return p_tri
