#!/usr/bin/python3
"""
This module is designed to test square.py
"""
import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
    Class to define the unittest
    """

    def test_var(self):
        """
        test class instance variables
        """
        s1 = Square(10)
        s2 = Square(5, 6, 10)
        # self.assertEqual(s1.id, 3)
        self.assertEqual(s1.size, 10)
        # self.assertEqual(s2.id, 4)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 6)
        self.assertEqual(s2.y, 10)
        with self.assertRaises(TypeError):
            b = Square()
        with self.assertRaises(ValueError):
            b = Square(-2)
        with self.assertRaises(TypeError):
            b = Square('foo')
        with self.assertRaises(ValueError):
            b = Square(5, -1, 0)
        with self.assertRaises(ValueError):
            b = Square(10, 10, -5)
        with self.assertRaises(TypeError):
            b = Square(5, 'foo', 0)
        with self.assertRaises(TypeError):
            b = Square(10, 10, 'bar')

    def test_area(self):
        """
        test class instance area method
        """
        sq1 = Square(10)
        sq2 = Square(5, 6, 10)
        self.assertEqual(sq1.area(), 100)
        self.assertEqual(sq2.area(), 25)
        with self.assertRaises(TypeError):
            sq1.area(7)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, stdout):
        """
        test class instance display method
        """
        r1 = Square(4)
        r1.display()
        extected_out = '####\n####\n####\n####\n'

        self.assertEqual(stdout.getvalue(), extected_out)

        r1 = Square(2, 2, 2)
        r1.display()
        extected_out = '\n\n  ##\n  ##\n'

    def test_str(self):
        """
        test class instance __str__ method
        """
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(print(r1), print('[Square] (12) 2/1 - 4'))

        r2 = Square(5, 1)
        self.assertEqual(print(r2), print('[Square] (1) 1/0 - 5'))
