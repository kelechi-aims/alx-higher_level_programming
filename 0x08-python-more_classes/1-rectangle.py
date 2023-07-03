#!/usr/bin/python3
'''
   A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
'''


class Rectangle:
    '''
    Represents a rectangle.
    '''

    def __init__(self, width=0, height=0):
        '''
        Initializes the rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Default to 0.
            height (int, optional): The height of the rectangle. Default to 0.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Sets the width of the rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If width is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        '''

        return self.__height

    @height.setter
    def height(self, value):
        '''
        Sets the height of the rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If height is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
