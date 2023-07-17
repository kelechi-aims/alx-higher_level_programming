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
        s = Square(10, 2, 3, 42)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 42)

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

        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

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

        s.update(20)
        self.assertEqual(s.id, 20)

        s.update(25, 8)
        self.assertEqual(s.id, 25)
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

        s.update(30, 4, 3)
        self.assertEqual(s.id, 30)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 3)

        s.update(35, 2, 2, 2)
        self.assertEqual(s.id, 35)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)

    def test_update_kwargs(self):
        """Test the update method of the Square class using **kwargs."""
        s = Square(5)
        s.update(id=42)
        self.assertEqual(s.id, 42)

        s.update(size=8)
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

        s.update(x=3)
        self.assertEqual(s.x, 3)

        s.update(y=2)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class."""
        s = Square(5, 2, 3, 10)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
