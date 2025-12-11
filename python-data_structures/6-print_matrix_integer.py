#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lin in matrix:
        for n in lin:
            print("{:d}".format(n), end=" ")
        print()
