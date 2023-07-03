#!usr/bin/python3
'''
   This contains a function that adds 2 integers.
   Return their sum.

'''


def add_integer(a, b=98):
    '''
    Adds two integers.

    Args:
        a (int or float): First number.
        b (int or float): Second number (default is 98).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    '''

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
