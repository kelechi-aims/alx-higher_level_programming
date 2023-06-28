#!/usr/bin/python3
""" A class Square that defines a square by:
    Private instance attribute: size
    stantiation with size (no type/value verification)
"""


class Square:
    """A class that defines a square.

    Attributes:
        __size (int): The size of the square (private).

    """

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
