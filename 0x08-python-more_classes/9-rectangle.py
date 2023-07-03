#!/usr/bin/python3
'''
   A class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
'''


class Rectangle:
    '''
    Represents a rectangle.
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        Initializes the rectangle instance.
        And increments the count of instances

        Args:
            width (int, optional): The width of the rectangle. Default to 0.
            height (int, optional): The height of the rectangle. Default to 0.
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        Computes and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        '''
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle representation b '#' characters.
        '''
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(
                [str(self.print_symbol) * self.__width] * self.__height
            )

    def __repr__(self):
        '''
        Returns a string representation of the rectangle.

        Returns:
            str: The representation of the rectangle object.
        '''
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        '''
        Prints a message when an instance of Rectangle is deleted.
        And decrements the count of instances
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        Compares two rectangles and returns the biggest based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle object.
            rect_2 (Rectangle): The second rectangle object.

        Returns:
            Rectangle: The rectangle with the bigger or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance
        '''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        '''
        Returns a new Rectangle instance with width == height == size

        Args:
            size (int): Width and height of the rectangle

        Returns:
            int: A new rectangle.
        '''
        return cls(size, size)
