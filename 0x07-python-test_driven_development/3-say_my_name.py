#!/usr/bin/python3
'''
   The function in this module prints My name is <first name> <last name>.
   In the above format

'''


def say_my_name(first_name, last_name=""):
    '''
    Prints the name based on the first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default to an empty string.

    Raises:
        TypeError: If either first_name or last-name is not a string.

    Returns:
        None
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
#    if last_name:
    print("My name is {} {}". format(first_name, last_name))
#    else:
#        print("My name is {}".format(first_name))
