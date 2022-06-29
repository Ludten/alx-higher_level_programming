#!/usr/bin/python3
"""
A module with a function for dividing a matrix with
an integer
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix with an integer

    Args:
        matrix (list)
        div (int)

    Raises:
        TypeError: if matrix is not a list of lists with integers
        TypeError: if matrix has inconsistent row count
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is 0

    Returns:
        a new matrix divided
    """
    if isinstance(matrix, list) is not True:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if matrix == [] or matrix == [[]]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for el in matrix:
        if isinstance(el, list) is not True:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for ele in el:
            if isinstance(ele, (int, float)) is not True:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
integers/floats")
    length = len(matrix[0])
    if any(len(lst) != length for lst in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, (int, float)) is not True:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_mat = [[round(j / div, 2) for j in i] for i in matrix]
    return new_mat
