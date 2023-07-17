#!/usr/bin/python3
'''This module has the test suite for Square class
'''
import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    '''
    Test suite for the Square class
    '''

    def test_constructor_with_size(self):
        '''
        Test constructor with size argument.
        '''
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_constructor_with_x_and_y(self):
        '''
        Test constructor with x and y arguments.
        '''
        s = Square(5, 2, 3)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        '''
        Test the area method of the Square class.
        '''
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s = Square(3, 1, 3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        '''
        Test the __str__ method of the square class.
        '''
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

        s = Square(3, 1, 3)
        self.assertEqual(str(s), "[Square] (2) 1/3 - 3")

    def test_display(self):
        '''
        Test the display method of the Square class.
        '''
        s = Square(5)
        output = "#####\n#####\n#####\n#####\n#####\n"
        with patch("sys.stdout", new=StringIO()) as buffer:
            s.display()
            self.assertEqual(buffer.getvalue(), output)

        s = Square(3, 1, 3)
        output = "\n\n\n ###\n ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as buffer:
            s.display()
            self.assertEqual(buffer.getvalue(), output)

    def test_update(self):
        '''
        Test the update method of the Square class.
        '''
        s = Square(5)

        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")

        s.update(10, 3)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 3")

        s.update(10, 3, 2)
        self.assertEqual(str(s), "[Square] (10) 2/0 - 3")

        s.update(10, 3, 2, 4)
        self.assertEqual(str(s), "[Square] (10) 2/4 - 3")

        s.update(10, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (10) 4/5 - 3")


if __name__ == "__main__":
    unittest.main()
