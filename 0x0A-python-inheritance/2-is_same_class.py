#!/usr/bin/python3
'''This module contains a function that returns True if the object is
   exactly an instance of the specified class: otherwise false
'''


def is_same_class(obj, a_class):
    '''
    Checks if the object's class is the same as the specified class
    '''
    return type(obj) is a_class
