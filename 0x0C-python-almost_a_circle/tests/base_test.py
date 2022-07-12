#!/usr/bin/python3
"""
This module is designed to test square.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Class to define the unittest
    """

    def test_id(self):
        """
        test class id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)


if __name__ == '__main__':
    unittest.main()
