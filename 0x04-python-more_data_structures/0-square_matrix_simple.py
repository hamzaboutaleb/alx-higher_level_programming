#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
	new_row = map(lambda x : x * x, row)
        result.append(new_row)
    return result
