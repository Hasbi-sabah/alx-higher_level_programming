#!/usr/bin/python3
#This is a function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for i in matrix:
        for j in i:
            if j == i[-1]:
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=' ')
