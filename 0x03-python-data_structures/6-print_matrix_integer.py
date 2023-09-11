#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """a script that prints a matrix of integers

    """

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if c != 0:
                print(" ", end='')
            print("{:d}".format(matrix[r][c]), end='')
        print()
