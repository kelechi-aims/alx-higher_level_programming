#!/usr/bin/python3
'''Has a function that returns the JSON representation of a object(string)
'''
import json


def to_json_string(my_obj):
    '''
    converts an object to its JSON representation as a string.

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    '''
    return json.dumps(my_obj)
