#!/usr/bin/python3
"""A function that divides all elements of a matrix
   matrix_divided: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """A function that divides all the elements of a matrix
        matrix (list): list of lists of integers or floats
        div (int/float): Value to divide by.
    Raises:
        TypeError: Matrix not a list of lists
        TypeError: Each row of the matrix isn't of the same size
        TypeError: Element of any list is not an integer or float
        TypeError: Row in the matrix is not a list
        TypeError: div is not an integer or a float
        ZeroDivisionError: div is equal to 0

    Returns: The result of the matrix division
    """
    row_size = None

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([[round(j / div, 2) for j in i] for i in matrix])
