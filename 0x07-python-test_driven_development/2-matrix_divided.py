#!/usr/bin/python3

def matrix_divided(matrix, div):
    """divide all elemn of matrix by number.
        Args:
            matrix (list): list of list of int/float.
            div (int/float): divisor
        Raises:
            TypeError: If the matrix contains non-numbers.
            TypeError: for differnet size of rows.
            TypeError: div not int or float
            ZeroDivisionError: If div is 0.
     """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix \
                    must have the same size")

    for i in range(len(matrix)):
        for el in matrix[i]:
            if not isinstance(el, int) and not isinstance(el, float):
                raise TypeError("matrix must be a matrix \
                        list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [x[:] for x in matrix]
    for row in new_matrix:
        for i in range(len(row)):
            row[i] = round(row[i]/div, 2)
    return new_matrix
