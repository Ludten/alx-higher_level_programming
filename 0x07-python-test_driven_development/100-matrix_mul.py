#!/usr/bin/python3
"""
A module with a function for multiplying two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices

    Args:
        m_a (list)
        m_b (list)

    Raises:
        TypeError: if any matrices is not a list, list of
        lists, has inconsistent row count or their elements
        are not integers or float
        ValueError: if any of the matrices are empty

    Returns:
        product of both matrices
    """
    if isinstance(m_a, list) is not True:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is not True:
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for el in m_a:
        if isinstance(el, list) is not True:
            raise TypeError("m_a must be a list of lists")
        for ele in el:
            if isinstance(ele, (int, float)) is not True:
                raise TypeError("m_a should contain only integers or floats")
    for el in m_b:
        if isinstance(el, list) is not True:
            raise TypeError("m_b must be a list of lists")
        for ele in el:
            if isinstance(ele, (int, float)) is not True:
                raise TypeError("m_b should contain only integers or floats")
    lena = len(m_a[0])
    lenb = len(m_b[0])
    if any(len(lst) != lena for lst in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(lst) != lenb for lst in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) == len(m_b):
        result = [[sum(a * b for a, b in zip(a_row, b_col))
                   for b_col in zip(*m_b)] for a_row in m_a]
    else:
        raise ValueError("m_a and m_b can't be multiplied")

    return result
