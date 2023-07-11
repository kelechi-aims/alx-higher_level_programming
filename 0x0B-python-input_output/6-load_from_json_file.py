#!/usr/bin/python3
'''Has a function that creates an Object from a “JSON file”
'''
import json


def load_from_json_file(filename):
    '''
    Creates a Object from a JSON file.

    Args:
        filename: The name of the JSON file to load.

    Returns:
        object: The object created from the JSON file.
    '''
    with open(filename, mode='r') as file:
        return json.load(file)
