#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        if len(i) > 0:
            new_matrix.append(list(map((lambda x: x**2), i)))
    return new_matrix
