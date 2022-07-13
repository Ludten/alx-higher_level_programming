#!/usr/bin/python3
"""
This module is designed to test square.py
"""
import unittest
import os
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

    def test_save_to_file(self):
        """
        test class instance save_to_file method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        PATH = './{}.json'.format(Rectangle.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Rectangle.__name__))
        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(cont, expected)
        r1 = Rectangle(5, 10, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        PATH = './{}.json'.format(Rectangle.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Rectangle.__name__))
        expected = '[{"id": 3, "width": 5, "height": 10, "x": 2, "y": 8}, \
{"id": 4, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(cont, expected)
        Rectangle.save_to_file(None)
        PATH = './{}.json'.format(Rectangle.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Rectangle.__name__))
        expected = '[]'
        self.assertEqual(cont, expected)
        Rectangle.save_to_file(())
        PATH = './{}.json'.format(Rectangle.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Rectangle.__name__))
        expected = '[]'
        self.assertEqual(cont, expected)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(2)
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file('foo')
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    @staticmethod
    def write_file(filename):
        """
        A function that opens and reads a file

        Args:
            filename (str)

        Returns:
            number of characters written into file
        """
        with open(filename, 'r', encoding="utf-8") as f:
            text = ""
            for line in f:
                text += line
            return text

    def test_from_json_string(self):
        """
        test class instance from_json_string method
        """
        jsonstr = '[{"id": 3, "width": 5, "height": 10, "x": 2, "y": 8}, \
{"id": 4, "width": 2, "height": 4, "x": 0, "y": 0}]'
        tlist = Rectangle.from_json_string(jsonstr)
        expected = [{"id": 3, "width": 5, "height": 10, "x": 2, "y": 8},
                    {"id": 4, "width": 2, "height": 4, "x": 0, "y": 0}]
        self.assertCountEqual(tlist, expected)
        jsonstr = ''
        tlist = Rectangle.from_json_string(jsonstr)
        expected = []
        self.assertCountEqual(tlist, expected)
        tlist = Rectangle.from_json_string(None)
        expected = []
        self.assertCountEqual(tlist, expected)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, stdout):
        """
        test class instance create method
        """
        dictionary = {"id": 3, "width": 3, "height": 5, "x": 1, "y": 0}
        r1 = Rectangle.create(**dictionary)
        print(r1)
        expected_out = '[Rectangle] (3) 1/0 - 3/5\n'
        self.assertEqual(stdout.getvalue(), expected_out)
        with self.assertRaises(TypeError):
            r1 = Rectangle.create(1)
        with self.assertRaises(TypeError):
            r1 = Rectangle.create('foo')
        with self.assertRaises(TypeError):
            r1 = Rectangle.create((4, 5))
        with self.assertRaises(TypeError):
            r1 = Rectangle.create(['foo'])
        r2 = Rectangle.create()
        self.assertEqual(r2, None)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create('foo', 5)

    def test_load_from_file(self):
        """
        test class instance load_from_file method
        """
        PATH = './{}.json'.format(Rectangle.__name__)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        tlist = Rectangle.load_from_file()
        for cl in tlist:
            self.assertEqual(isinstance(cl, Rectangle), True)
        with self.assertRaises(TypeError):
            nlist = Rectangle.load_from_file(5)
        os.remove(PATH)

        if os.path.isfile(
                PATH) and os.access(PATH, os.R_OK) is False:
            nolist = Rectangle.load_from_file()
            self.assertCountEqual(nolist, [])

    def test_csv(self):
        """
        test class instance csv method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        PATH = './{}.csv'.format(Rectangle.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        content = self.write_file('{}.csv'.format(Rectangle.__name__))
        expected_out = '1,10,7,2,8\n2,2,4,0,0\n'
        self.assertEqual(content, expected_out)

        rec1 = Rectangle(5, 10, 2, 8)
        rec2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([rec1, rec2])
        PATH = './{}.csv'.format(Rectangle.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.csv'.format(Rectangle.__name__))
        expected = '3,5,10,2,8\n4,2,4,0,0\n'
        self.assertEqual(cont, expected)
        Rectangle.save_to_file_csv(None)
        PATH = './{}.csv'.format(Rectangle.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.csv'.format(Rectangle.__name__))
        expected = ''
        self.assertEqual(cont, expected)
        with self.assertRaises(Exception):
            Rectangle.save_to_file_csv(())
        self.assertEqual(cont, expected)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(2)
        with self.assertRaises(Exception):
            Rectangle.save_to_file_csv('foo')
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        tlist = Rectangle.load_from_file_csv()
        for cl in tlist:
            self.assertEqual(isinstance(cl, Rectangle), True)
        with self.assertRaises(TypeError):
            nlist = Rectangle.load_from_file_csv(5)
        os.remove(PATH)

        if os.path.isfile(
                PATH) and os.access(PATH, os.R_OK) is False:
            nolist = Rectangle.load_from_file_csv()
            self.assertCountEqual(nolist, [])
