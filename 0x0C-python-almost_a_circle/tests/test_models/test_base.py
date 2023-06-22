#!/usr/bin/python3
"""base class Test module"""

import unittest
import pep8
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_without_id(self):
        """ test without setting id"""
        base = Base()
        b = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(b.id, 2)
    
    def test_with_id(self):
        """ test setting id """
        b = Base(15)
        self.assertEqual(b.id, 15)

if __name__ == "__main__":
    unittest.main()
