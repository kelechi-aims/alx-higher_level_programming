#!/usr/bin/python3
'''This module has test for the Base class
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test suite for the Base class.'''
    
    def test_id_increment(self):
        '''
        Test that the id increments correctly for multiple
        instances of Base.
        '''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        '''
        Test that a custom id is correctly assigned to the instance.
        '''
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_increment_after_custom_id(self):
        '''
        Test that the id increments correctly after a custom id.
        '''
        b1 = Base()
        self.assertEqual(b1.id, 4)

if __name__ == "__main__":
    unittest.main()
