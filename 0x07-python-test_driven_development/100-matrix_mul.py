#!/usr/bin/python3
'''
   This module has a function that multiplies 2 matrices
'''


def matrix_mul(m_a, m_b):
    '''
    Multiplies two matrices.

    Args:
        m_a (list): The first matrix represented as a list of lists
                    of integers or floats.
        m_b (list): The second matrix represented as a list of lists
                    of integers or floats.

    Returns:
        list: The result of multiplying the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list,
                   or if m_a or m_b is not a list of lists,
                   or if one element of the matrices is not an integer
                   or float,
                   or if m_a or m_b is not a rectangle
                   (rows of different sizes).
        ValueError: If m_a or m_b is empty ([] or [[]]),
                    or if m_a and m_b cannot be multiplied.

    '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_a can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
        for row_a in m_a
    ]
    return result
