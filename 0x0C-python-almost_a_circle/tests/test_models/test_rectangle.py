#!/usr/bin/python3
"""
This module is designed to test square.py
"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """
    Class to define the unittest
    """

    def test_var(self):
        """
        test class instance variables
        """
        b1 = Rectangle(10, 2)
        b2 = Rectangle(5, 6, 10, 5)
        # self.assertEqual(b1.id, 3)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 2)
        # self.assertEqual(b2.id, 4)
        self.assertEqual(b2.width, 5)
        self.assertEqual(b2.height, 6)
        self.assertEqual(b2.x, 10)
        self.assertEqual(b2.y, 5)
        with self.assertRaises(TypeError) as cm:
            b3 = Rectangle(15)
        with self.assertRaises(TypeError):
            b = Rectangle()
        with self.assertRaises(ValueError):
            b = Rectangle(15, -1)
        with self.assertRaises(ValueError):
            b = Rectangle(-2, 10)
        with self.assertRaises(TypeError):
            b = Rectangle('foo', 5)
        with self.assertRaises(TypeError):
            b = Rectangle(10, "5")
        with self.assertRaises(ValueError):
            b = Rectangle(15, 5, -1, 0)
        with self.assertRaises(ValueError):
            b = Rectangle(8, 10, 10, -5)
        with self.assertRaises(TypeError):
            b = Rectangle(15, 5, 'foo', 0)
        with self.assertRaises(TypeError):
            b = Rectangle(8, 10, 10, 'bar')

    def test_area(self):
        """
        test class instance area method
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(5, 6, 10, 5)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 30)
        with self.assertRaises(TypeError):
            r1.area(7)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, stdout):
        """
        test class instance display method
        """
        r1 = Rectangle(4, 6)
        r1.display()
        extected_out = '####\n####\n####\n####\n####\n####\n'

        self.assertEqual(stdout.getvalue(), extected_out)

        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        extected_out = '\n\n  ##\n  ##\n  ##\n'

    def test_str(self):
        """
        test class instance __str__ method
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(print(r1), print('[Rectangle] (12) 2/1 - 4/6'))

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(print(r2), print('[Rectangle] (1) 1/0 - 5/5'))
