#!/usr/bin/python3
import numpy as np
'''
   This module has afunction that multiplies 2 matrices by using the module
   NumPy
'''


def lazy_matrix_mul(m_a, m_b):
    '''
    Multiplies two matrices using the NumPy module and returns the result.

    Args:
    m_a (list): The first matrix represented as a list
                of lists of integers or floats.
    m_b (list): The second matrix represented as a list
                of lists of integers or floats.

    Returns:
        list: The resulting matrix after multiplying m_a and m_b.

    Raises:
        ValueError: If m_a or m_b is empty ([] or [[]]),
                    or if the matrices cannot be multiplied.
    '''
    result = np.matmul(m_a, m_b)
    return result
