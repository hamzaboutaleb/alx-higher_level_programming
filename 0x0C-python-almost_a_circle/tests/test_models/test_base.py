#!/usr/bin/python3
"""base class Test module"""

import unittest
import pep8
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_without_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
    
    def test_with_id(self):
        b = Base(15)
        self.assertEqual(b.id, 15)

    def test_pep8_model(self):
        """Tests for pep8 model"""

        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
