#!/usr/bin/python3
# This is a function that computes
# the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda row: list(map(lambda x: x*x, row)), matrix))
    return new_matrix
