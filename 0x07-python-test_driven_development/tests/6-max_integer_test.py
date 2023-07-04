#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Unittests for the function max_integer(list=[]).'''
    def test_empty_list(self):
        '''Test max_integer with an empty list'''
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        '''Test max_integer with a list containing a single element'''
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_number(self):
        '''Test max_integer with a list of positive numbers'''
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        '''Test max_integer with] a list of negative numbers'''
        result = max_integer([-5, -4, -3, -2, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        '''Test max_integer with a list of mixed positive
        and negative numbers.
        '''
        result = max_integer([-5, 0, 10, 2, 7])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        '''Test max_integer with a list containing duplicated numbers'''
        result = max_integer([2, 4, 6, 4, 2])
        self.assertEqual(result, 6)

    def test_float_numbers(self):
        '''Test max_integer with a list of float numbers'''
        result = max_integer([1.5, 2.7, 3.9, 2.1])
        self.assertEqual(result, 3.9)

    def test_no_arg(self):
        '''Test max_integer with no argument'''
        self.assertEqual(max_integer(), None)

    def test_identical(self):
        '''Test max_integer with list of identical numbers'''
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_strings(self):
        '''Test with string as argument'''
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")
        self.assertEqual(max_integer(["cat", "dog", "elephant"]), "elephant")

    def test_large_numbers(self):
        '''Test max_integer with large numbers'''
        self.assertEqual(max_integer([10**10, 10**20, 10**30]), 10**30)
        self.assertEqual(max_integer([-10**10, -10**20, -10**30]), -10**10)

    def test_none_value(self):
        '''Test max_integer with None as an element of a list''' 
        with self.assertRaises(TypeError):
             max_integer([None, 1, 2])

    def test_exception(self):
        '''Test max_integer for exceptions'''
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three"])


if __name__ == '__main__':
    unittest.main()
