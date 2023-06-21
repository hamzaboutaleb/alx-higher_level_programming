#!/usr/bin/python3
"""base class Test module"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_without_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
    
    def test_with_id(self):
        b = Base(15)
        self.assertEqual(b.id, 15)


if __name__ == "__main__":
    unittest.main()
