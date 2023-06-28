#!/usr/bin/python3
""" A class Square that defines a square by:(based on 4-square.py)
"""


class Square:
    """ A class thats defines a square.

    Attributes:
        __size (int): The size of the square (private).

    """

    def __init__(self, size=0):
        """ Initializes a Square instance.

        Args:
            size (float or int, optional): The size of the square.
                Default to 0.

        Raises:
            TypeError: If size is not an number.
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """ Retrieve the size of the square.

        Returns:
            float or int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If value is not an number.
            ValueError: If value is less than 0.

        """
        if isinstance(value, (float, int)):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an number")

    def area(self):
        """ Calculates the area of the square.

        Returns:
            float or int: The area of the square.

        """
        return self.__size ** 2

    def __eq__(self, other):
        """ Compare if two squares are equal in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the squares are equal in area, False otherwise.

        """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Compare if two squares are not equal in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the squares are not equal in area, False otherwise.

        """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Compare if one squares is greater than the other in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is greater in area,
                False otherwise

        """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Compare if one squares is greater than or equal to the other
            in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is greater than or equal
                in area, False otherwise

        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ Compare if one squares is less than the other in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is less in area, False otherwise

        """
        return self.area() < other.area()

    def __le__(self, other):
        """ Compare if one squares is less than or equal to the other
            in terms of area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is less than or equal
                in area, False otherwise

        """
        return self.area() <= other.area()
