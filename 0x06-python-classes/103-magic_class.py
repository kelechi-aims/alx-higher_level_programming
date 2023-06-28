#!/usr/bin/python3
import math
""" Write the Python class MagicClass """


class MagicClass:
    """ A class representing a magic circle.

    Attributes:
        __radius (float): The radius of the magic circle.

    """
    def __init__(self, radius=0):
        """ Initializes a MagicCLass instance with a given radius.

        Args:
            Radius (float, optional): The radius of the magic circle.
                Defaults to 0.

        Raises:
            TypeError: If the radius is not a number (int, float).

        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Calculates the area of the magic circle.

        Returns:
            float: The area of the magic circle.

        """
        return ((self.__radius ** 2) * math.pi)

    def circunference(self):
        """ Calculates the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.

        """
        return 2 * math.pi * self.__radius
