#!/usr/bin/python3
"""Has a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object is it's possible.

    Args:
        obj: The object to add the attribute to.
        attr (str): The attribute name.
        value: the attribute value.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
