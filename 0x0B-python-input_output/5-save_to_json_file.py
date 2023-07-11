#!/usr/bin/python3
'''Has a function that writes an Object to a text file, using a JSON
   representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an object to a text file using its JSON representation

    Args:
        my_obj: The object to write to the file.
        filename: The name of the file to write the JSON representation to

    Returns:
        None
    '''
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
