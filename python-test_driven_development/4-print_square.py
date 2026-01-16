#!/usr/bin/python3
"""
Module provides a function that prints a square with the character #
Includes type checking

"""


def print_square(size):
    """
    receive one argument (size):
    size = a int who will define the size of the square

    return:
        a square made of #

    raise:
        TypeError: if not int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for largura in range(size):
        print("#" * int(size))
