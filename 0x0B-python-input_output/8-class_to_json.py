#!/usr/bin/python3
'''Has a function that returns the dictionary description with simple
   data structure (list, dictionary, string, integer and boolean) for
   JSON serialization of an object
'''
import json


def class_to_json(obj):
    '''
    Returns a dictionary description with a simple data structure.

    Args:
        obj: Aninstance of a class

    Returns:
        dict: The dictionary description of the object's attribute.
    '''
    json_dict = {}
    if hasattr(obj, "__dict__"):
        json_dict = obj.__dict__.copy()
    return json_dict