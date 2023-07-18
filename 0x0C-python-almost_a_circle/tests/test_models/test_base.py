#!/usr/bin/python3
'''This module has test for the Base class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string_empty(self):
        """Test to_json_string method with an empty list of dictionaries."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string method with None as the input."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_single_dict(self):
        """Test to_json_string method with a single dictionary."""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_to_json_string_multiple_dicts(self):
        """Test to_json_string method with multiple dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 3, 1)
        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()
        json_string = Base.to_json_string([dict1, dict2])
        self.assertEqual(json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 1, "width": 5, "id": 2, "height": 3, "y": 0}]')

    def test_to_json_string_empty_dict(self):
        """Test to_json_string method with an empty dictionary."""
        json_string = Base.to_json_string([{}])
        self.assertEqual(json_string, '[{}]')
        

if __name__ == "__main__":
    unittest.main()
