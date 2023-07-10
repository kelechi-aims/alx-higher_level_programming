#!/usr/bin/python3
'''This module has the function that the checks the kind of class'''


def is_kind_of_class(obj, a_class):
    '''
    Checks if an object is an instance of, or if the object is an instance
    that inherited from, the specified class.

    Args:
        obj: The object to check
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of the specified class or
        False otherwise.
    '''
    return isinstance(obj, a_class)
