#!/usr/bin/python3
""" A class Square that defines a square by:(based on 3-square.py)
"""


class Square:
    """ A class thats defines a square.

    Attributes:
        __size (int): The size of the square (private).

    """

    def __init__(self, size=0):
        """ Iniializes a Square instance.

        Args:
            size (int, optional): The size of the square. Default to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """ Retrieve the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
