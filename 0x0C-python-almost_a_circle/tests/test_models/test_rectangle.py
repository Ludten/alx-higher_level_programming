#!/usr/bin/python3
"""
This module is designed to test square.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """
    Class to define the unittest
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_var(self):
        """
        test class instance variables
        """
        b1 = Rectangle(10, 2)
        b2 = Rectangle(5, 6, 10, 5)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.width, 5)
        self.assertEqual(b2.height, 6)
        self.assertEqual(b2.x, 10)
        self.assertEqual(b2.y, 5)
        with self.assertRaises(TypeError):
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
        with self.assertRaises(TypeError):
            b = Rectangle(8, 10, 10, 15, 20, 25)

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
        with self.assertRaises(TypeError):
            r1.display(5)
        stdout.truncate(0)
        stdout.seek(0)

        r2 = Rectangle(2, 3, 2, 2)
        r2.display()
        extected_out = '\n\n  ##\n  ##\n  ##\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, stdout):
        """
        test class instance __str__ method
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        expected_out = '[Rectangle] (12) 2/1 - 4/6\n'
        self.assertEqual(stdout.getvalue(), expected_out)
        stdout.truncate(0)
        stdout.seek(0)

        r2 = Rectangle(5, 5, 1)
        print(r2)
        expected_out = '[Rectangle] (1) 1/0 - 5/5\n'
        self.assertEqual(stdout.getvalue(), expected_out)
        stdout.truncate(0)
        stdout.seek(0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, stdout):
        """
        test class instance update method
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        print(r1)
        extected_out = '[Rectangle] (89) 10/10 - 10/10\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(89, 2)
        print(r1)
        extected_out = '[Rectangle] (89) 10/10 - 2/10\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(89, 2, 3)
        print(r1)
        extected_out = '[Rectangle] (89) 10/10 - 2/3\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(89, 2, 3, 4)
        print(r1)
        extected_out = '[Rectangle] (89) 4/10 - 2/3\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        extected_out = '[Rectangle] (89) 4/5 - 2/3\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(height=1)
        print(r1)
        extected_out = '[Rectangle] (89) 4/5 - 2/1\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(width=1, x=2)
        print(r1)
        extected_out = '[Rectangle] (89) 2/5 - 1/1\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(y=1, width=2, x=3, id=89)
        print(r1)
        extected_out = '[Rectangle] (89) 3/1 - 2/1\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(x=1, height=2, y=3, width=4)
        print(r1)
        extected_out = '[Rectangle] (89) 1/3 - 4/2\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(7, 8, 9, y=1, width=2, x=3, id=89)
        print(r1)
        extected_out = '[Rectangle] (7) 1/3 - 8/9\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)

    def test_to_dict(self):
        """
        test class instance to_dictionary method
        """
        r1 = Rectangle(10, 2, 1, 9)
        expected_out = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(type(r1.to_dictionary()), type(expected_out))
        self.assertDictEqual(r1.to_dictionary(), expected_out)

        r2 = Rectangle(1, 1)
        expected_out = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(type(r2.to_dictionary()), type(expected_out))
        self.assertDictEqual(r2.to_dictionary(), expected_out)

    def test_to_json_string(self):
        """
        test class instance to_json_string method
        """
        tdict = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(Rectangle.to_json_string([tdict]), expected)
        with self.assertRaises(TypeError):
            Rectangle.to_json_string([tdict], [])
        tdict = {"x": 2, "size": 10, "id": 1, "y": 8}
        expected = '[{"x": 2, "size": 10, "id": 1, "y": 8}]'
        self.assertEqual(Rectangle.to_json_string([tdict]), expected)
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string(None), "[]")
