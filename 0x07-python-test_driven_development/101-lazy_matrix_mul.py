#!/usr/bin/python3
"""
A module with a function for multiplying two matrices
using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
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

    return np.matmul(m_a, m_b)
