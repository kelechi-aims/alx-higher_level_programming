#!/usr/bin/python3
'''
   This module has a function that returns the list of available attributes
   and methods of an object
'''


def lookup(obj):
    '''Gets the list of attributes and methods of the object'''
    attributes = dir(obj)
    return attributes
