#!/usr/bin/python3
'''This module has test for the Base class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


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
    
    def setUp(self):
        """Set up method to run before each test."""
        # Remove any existing Rectangle.json file before each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        """Tear down method to run after each test."""
        # Remove the created Rectangle.json file after each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file method with None as input."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file method with an empty list."""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_single_instance(self):
        """Test save_to_file method with a single instance."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"width": 10', content)
            self.assertIn('"height": 7', content)
            self.assertIn('"x": 2', content)
            self.assertIn('"y": 8', content)

    def test_save_to_file_multiple_instances(self):
        """Test save_to_file method with multiple instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"width": 10', content)
            self.assertIn('"height": 7', content)
            self.assertIn('"x": 2', content)
            self.assertIn('"y": 8', content)
            self.assertIn('"id": 2', content)
            self.assertIn('"width": 2', content)
            self.assertIn('"height": 4', content)
            self.assertIn('"x": 0', content)
            self.assertIn('"y": 0', content)
        
    def test_from_json_string_none(self):
        """Test from_json_string method with None as input."""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty(self):
        """Test from_json_string method with an empty string as input."""
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        """Test from_json_string method with valid JSON string."""
        json_str = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        expected_result = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        result = Base.from_json_string(json_str)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
