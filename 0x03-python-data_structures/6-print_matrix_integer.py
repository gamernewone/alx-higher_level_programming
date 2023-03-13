#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:

        for y in i:

            if y == i[len(i) - 1]:
                print("{:d}$".format(y))

            else:
                print("{:d}".format(y), end=" ")
