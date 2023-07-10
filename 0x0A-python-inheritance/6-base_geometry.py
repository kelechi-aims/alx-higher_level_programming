#!/usr/bin/python3
'''has a class basegeometry based on 5-base_geometry'''


class BaseGeometry:
    '''
    Base class for geometry objects.

    Publuc Methods:
        area() - Raises an Exception
    '''
    def area(self):
        '''
        calculates the area of the geometry object.

        Raises:
            Exception: Always raises an Exception
        '''
        raise Exception("area() is not implemented")
