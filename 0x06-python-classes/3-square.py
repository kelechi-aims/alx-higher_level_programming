#!/usr/bin/python3
""" A class Square that defines a square by:
    Private instance attribute: size
    Instantiation with optional size
"""


class Square:
    """ A class that difines a square.

    Attributes:
        __size (int): The size of the square (private).

    """

    def __init__(self, size=0):
        """ Initialize a Square instance.

        Args:
            size (int, optional): The size of square.Default to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
            """ Calculates he area of he square.

            Returns:
                int: The area of the square.
            """
            return self.__size * 2
