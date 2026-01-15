#!/usr/bin/python3
"""
Module provides a function that divides a matrix by the indicated value
Includes type checking and handle float numbers

"""


def matrix_divided(matrix, div):
    """
    adds two objects
    args:
    matrix = matrix (list of lists) of integers/floats
    div = divider who will divide the matrix

    return:
        the matrix made of list of lists divided by "div"

    raise:
        TypeError: if div or matrix not int or float,
                    if matrix sizes are not equal,
                        matrix not a list of lists.
        ZeroDivisionError: if div == 0
    """
    result = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div != div or div == float('inf') or div == float('-inf'):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrixlist = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrixlist)

    if not all(isinstance(x, list) for x in matrix):
        raise TypeError(matrixlist)

    for x in matrix:
        row_matrix = len(matrix[0])
        if len(x) != row_matrix:
            raise TypeError("Each row of the matrix must have the same size")

        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError(matrixlist)

        matrix_result = list(map(lambda y: round(y / div, 2), x))
        result.append(matrix_result)

    return result
