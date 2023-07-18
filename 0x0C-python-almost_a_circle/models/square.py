#!/usr/bin/pythona
'''This module has class Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class that inherits from the Rectangle class.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The id of the square.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
                               Default to 0.
            y (int, optional): The y-coordinate of the square's position.
                               Default to 0.
            id (int, optional): The id of the square. Default to None.
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        setter for the size attribute.

        Args:
            value (int): The size value to assign.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        Returns the string representation of the square.
        '''
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        '''
        Updates the attributes of the square.

        Args:
            *args: is the list of arguments - no-keyworded arguments
            1st argument: id attribute
            2nd argument: size attribute
            3rd argument: the x-coordinate of the square's position
            4th argument: the y-coordinate of the square's position
        '''
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of a square.
        '''
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
