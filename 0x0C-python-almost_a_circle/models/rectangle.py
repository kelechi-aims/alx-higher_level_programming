#!/usr/bin/python3
'''This module has the class Rectangle that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class that inherits from the Base class..

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The id of the rectangle.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's
                              position. Default to 0.
            y (int, optional): The y-coordinate of the rectangle's
                               position. Default to 0.
            id (int): The id of the rectangle. Default to None.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Getter for the width attribute

        Returns:
            int: The width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for the width attribute.

        Args:
            value (int): The width value to assign.

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Getter for the height attribute

        Returns:
            int: The height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for the height attribute.

        Args:
            value (int): The height value to assign.

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Getter for the x-coordinate attribute.

        Returns:
            int: the x-coordinate of the rectangle's position
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for the x-coordinate attribute.

        Args:
            value (int): The x-coordinate value to assign.

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Getter of the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter of the y-coordinate attribute.

        Args:
            value (int): The y-coordinate value to assign.

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        '''
        return self.width * self.height

    def display(self):
        '''
        Prints in stdout the Rectangle instance with the character #.
        '''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''
        Returns the string representation of the rectangle.
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        '''
        Updates the attributes of the rectangle.

        Args:
            *args: Variable number of arguments in the order:
                1st argument: id attribute
                2nd argument: width attribute
                3rd argument: height attribute
                4th argument: x attribute
                5th argument: y attribute
            **kwargs: Variable number of keyword arguments.
        '''
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns the dictionary repesentation of a rectangle.
        '''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
