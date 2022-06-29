#!/usr/bin/python3
"""
This module is designed to test 6-max_integer_test.py
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class to define the unittest
    """

    def test_values(self):
        """
        check elements type
        """
        with self.assertRaises(TypeError):
            max_integer([1, 'fg', 3, 4])

    def test_empty(self):
        """
        check list size
        """
        self.assertAlmostEqual(max_integer(), None)

    def test_large(self):
        """
        check return
        """
        self.assertAlmostEqual(max_integer([1, 2, 45, 4]), 45)
        self.assertAlmostEqual(max_integer((1, 2, 3)), 3)
        self.assertAlmostEqual(max_integer("string"), 't')
