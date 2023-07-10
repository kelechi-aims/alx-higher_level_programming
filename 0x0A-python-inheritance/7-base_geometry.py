#!/usr/bin/python3
'''has a class basegeometry based on 5-base_geometry'''


class BaseGeometry:
    '''
    Base class for geometry objects.

    Public Methods:
        area() - Raises an Exception
        integer_validator(name, value) - validates value.
    '''
    def area(self):
        '''
        calculates the area of the geometry object.

        Raises:
            Exception: Always raises an Exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validates that a value is an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Returns:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
