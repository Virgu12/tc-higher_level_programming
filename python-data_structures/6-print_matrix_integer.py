#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for linha in matrix:
        print(" ".join("{:d}".format(n) for n in linha))
