#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds 2 tuples, we append (0, 0) to ensure the each
    tuple has the length of at least 2
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
