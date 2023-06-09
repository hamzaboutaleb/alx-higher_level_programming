#!/usr/bin/python3
"""unit test for max_integere """


import unittest

max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """unit test for max integer function"""

    def test_max_integer_at_begginning(self):
        """test for max integer at the beginning of list"""

        self.assertEqual(max_integer([10, 1, 5, 0]), 10)

    def test_max_ordered_list(self):
        """ test for ordered list"""
        self.assertEqual(max_integer([1, 5, 8, 9]), 9)

    def test_max_at_middle_list(self):
        """test for max integer at the middle"""
        self.assertEqual(max_integer([1, 9, 2, 4]), 9)

    def test_empty_list(self):
        """test for empty list"""
        self.assertEqual(max_integer([]), None)
    
    def test_max_float(self):
        """test for float number list"""
        self.assertEqual(max_integer([15.6, 19.2, 20.0]), 20.0)
 
if __name__ == "__main__":
    unittest.main()
