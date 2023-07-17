#!/usr/bin/python3
'''This module has the test cases for Rectangle class'''
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    '''Test suite for the Rectangle class.'''

    def test_rectangle_creation(self):
        '''
        Test that a Rectangle instance is created with the correct id
        '''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_getters_setters(self):
        '''
        Test the getters and setters for the width, height, x and y
        attributes.
        '''
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r.width = 20
        r.height = 8
        r.x = 2
        r.y = 3
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_width_type_error(self):
        '''
        Test that a TypeError is raised if width is not an integer.
        '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 5)
            r.width = "invalid"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_value_error(self):
        '''
        Test that a ValueError is raised if width is <= 0.
        '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 5)
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_heiht_type_error(self):
        '''
        Test that a TypeError is raised if height is not an integer.
        '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 5)
            r.height = "invalid"
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_value_error(self):
        '''
        Test that a ValueError is raised if height is <= 0.
        '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 5)
            r.height = -5
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_type_error(self):
        '''
        Test that a TypeError is raised if x is not an integer.
        '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 5)
            r.x = "invalid"
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_value_error(self):
        '''
        Test that a ValueError is raised if x is < 0.
        '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 5)
            r.x = -2
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_type_error(self):
        '''
        Test that a TypeError is raised if y is not an integer.
        '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 5)
            r.y = "invalid"
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_value_error(self):
        '''
        Test that a ValueError is raised if y is < 0.
        '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 5)
            r.y = -4
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        '''
        Test the area method of the Rectangle class.
        '''
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        '''
        Test the display method of the Rectangle class.
        '''
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as buffer:
            r1.display()
            self.assertEqual(buffer.getvalue(), expected_output)

        r2 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as buffer:
            r2.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_str(self):
        '''
        Test the __str__ method of the Rectangle class.
        '''
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")


if __name__ == "__main__":
    unittest.main()
