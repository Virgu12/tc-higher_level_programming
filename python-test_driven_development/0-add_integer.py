#!/usr/bin/python3
"""
Module provides a function that adds two integers
Includes type checking and handle float numbers

"""


def add_integer(a, b=98):
    """
    Add two integers
    args:
    a = float or integer number
    b = float or integer number (98 if None)

    return:
        the integer result of a and b adding

    raise:
        TypeError: if a or b not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
