#!/usr/bin/python3
'''This module has the function that the checks class inheritance'''


def inherits_from(obj, a_class):
    '''
    Checks if an object is an instance of a class  that inherited from
    the specified class.

    Args:
        obj: The object to check
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance ofa subclass the specified class
        or False otherwise.
    '''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
