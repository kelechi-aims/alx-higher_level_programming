#!/usr/bin/python3
""" A class Square that defines a square by:(based on 3-square.py)
"""


class Square:
    """ A class thats defines a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).

    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Default to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than 0 or position contains negative.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrieve the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position od the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple or contains non-integer values.
            ValueError: If value contains negative values.

        """
        if isinstance(value, tuple) and len(value) == 2 and all(
            isinstance(num, int) for num in value
        ):
            if all(num >= 0 for num in value):
                self.__position = value
            else:
                raise ValueError(
                    "position must be a tuple of 2 positive integers"
                )
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square using the # character.

        If size is 0, an empty line is printed.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
