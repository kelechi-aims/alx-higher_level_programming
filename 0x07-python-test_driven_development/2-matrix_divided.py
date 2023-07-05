#!/usr/bin/python3
'''
   This contains a function that divides all elements of a matrix.
   Returns a new matrix.

'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list
                       of lists of integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with all elements divided by div,
              rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a matrix (list of lists) of integers/floats
               or if each row of the matrix does not have the same size,
               or if div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.

    '''

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return m
