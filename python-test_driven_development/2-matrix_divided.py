#!/usr/bin/python3
"""Module that divides all elements of a matrix by a given divisor."""


def matrix_divided(matrix, div):
    """Divide every element of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: a list of lists of integers or floats.
        div: the number (integer or float) to divide each element by.

    Returns:
        A new matrix with each element divided by div and rounded to
        2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If the rows of matrix don't all have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(err_matrix)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
