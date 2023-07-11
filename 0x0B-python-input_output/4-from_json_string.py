#!/usr/bin/python3
'''Has a function that returns an object (Python data structure)
   represented by a JSON string
'''
import json


def from_json_string(my_str):
    '''
    Converts a JSON to its corresponding Python data structure.

    Args:
        my_str: The JSON string to convert.

    Returns:
        object: The Python data structure represented by the string.
    '''
    return json.loads(my_str)
