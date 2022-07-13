#!/usr/bin/python3
"""
This module is designed to test square.py
"""
import unittest
import os
from models.square import Square
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
    Class to define the unittest
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_var(self):
        """
        test class instance variables
        """
        s1 = Square(10)
        s2 = Square(5, 6, 10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s2.id, 2)
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
        with self.assertRaises(TypeError):
            b = Square(10, 10, 15, 20, 25)

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
        with self.assertRaises(TypeError):
            r1.display(5)
        stdout.truncate(0)
        stdout.seek(0)

        r1 = Square(2, 2, 2)
        r1.display()
        extected_out = '\n\n  ##\n  ##\n'
        stdout.truncate(0)
        stdout.seek(0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, stdout):
        """
        test class instance __str__ method
        """
        r1 = Square(4, 2, 1, 12)
        print(r1)
        expected_out = '[Square] (12) 2/1 - 4\n'
        self.assertEqual(stdout.getvalue(), expected_out)
        stdout.truncate(0)
        stdout.seek(0)

        r2 = Square(5, 1)
        print(r2)
        expected_out = '[Square] (1) 1/0 - 5\n'
        self.assertEqual(stdout.getvalue(), expected_out)
        stdout.truncate(0)
        stdout.seek(0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, stdout):
        """
        test class instance update method
        """
        r1 = Square(10, 10, 10)
        r1.update(89)
        print(r1)
        extected_out = '[Square] (89) 10/10 - 10\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(89, 2)
        print(r1)
        extected_out = '[Square] (89) 10/10 - 2\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(89, 2, 3)
        print(r1)
        extected_out = '[Square] (89) 3/10 - 2\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(89, 2, 3, 4)
        print(r1)
        extected_out = '[Square] (89) 3/4 - 2\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(size=1)
        print(r1)
        extected_out = '[Square] (89) 3/4 - 1\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(size=1, x=2)
        print(r1)
        extected_out = '[Square] (89) 2/4 - 1\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(y=1, size=2, x=3, id=89)
        print(r1)
        extected_out = '[Square] (89) 3/1 - 2\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)
        r1.update(7, 8, 9, y=1, size=2, x=3, id=89)
        print(r1)
        extected_out = '[Square] (7) 9/1 - 8\n'
        self.assertEqual(stdout.getvalue(), extected_out)
        stdout.truncate(0)
        stdout.seek(0)

    def test_to_dict(self):
        """
        test class instance to_dictionary method
        """
        r1 = Square(10, 1, 9)
        expected_out = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        self.assertEqual(type(r1.to_dictionary()), type(expected_out))
        self.assertDictEqual(r1.to_dictionary(), expected_out)

        r2 = Square(1)
        expected_out = {'x': 0, 'y': 0, 'id': 2, 'size': 1}
        self.assertEqual(type(r2.to_dictionary()), type(expected_out))
        self.assertDictEqual(r2.to_dictionary(), expected_out)

    def test_to_json_string(self):
        """
        test class instance to_json_string method
        """
        tdict = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(Square.to_json_string([tdict]), expected)
        with self.assertRaises(TypeError):
            Square.to_json_string([tdict], [])
        tdict = {"x": 2, "size": 10, "id": 1, "y": 8}
        expected = '[{"x": 2, "size": 10, "id": 1, "y": 8}]'
        self.assertEqual(Square.to_json_string([tdict]), expected)
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string(None), "[]")

    def test_save_to_file(self):
        """
        test class instance save_to_file method
        """
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        PATH = './{}.json'.format(Square.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Square.__name__))
        expected = '[{"id": 1, "size": 10, "x": 2, "y": 8}, \
{"id": 2, "size": 2, "x": 0, "y": 0}]'
        self.assertEqual(cont, expected)
        r1 = Square(5, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        PATH = './{}.json'.format(Square.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Square.__name__))
        expected = '[{"id": 3, "size": 5, "x": 2, "y": 8}, \
{"id": 4, "size": 2, "x": 0, "y": 0}]'
        self.assertEqual(cont, expected)
        Square.save_to_file(None)
        PATH = './{}.json'.format(Square.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Square.__name__))
        expected = '[]'
        self.assertEqual(cont, expected)
        Square.save_to_file(())
        PATH = './{}.json'.format(Square.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.json'.format(Square.__name__))
        expected = '[]'
        self.assertEqual(cont, expected)
        with self.assertRaises(TypeError):
            Square.save_to_file(2)
        with self.assertRaises(AttributeError):
            Square.save_to_file('foo')
        with self.assertRaises(TypeError):
            Square.save_to_file()

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
        tlist = Square.from_json_string(jsonstr)
        expected = [{"id": 3, "width": 5, "height": 10, "x": 2, "y": 8},
                    {"id": 4, "width": 2, "height": 4, "x": 0, "y": 0}]
        self.assertCountEqual(tlist, expected)
        jsonstr = ''
        tlist = Square.from_json_string(jsonstr)
        expected = []
        self.assertCountEqual(tlist, expected)
        tlist = Square.from_json_string(None)
        expected = []
        self.assertCountEqual(tlist, expected)
        with self.assertRaises(TypeError):
            Square.from_json_string()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, stdout):
        """
        test class instance create method
        """
        dictionary = {"id": 3, "size": 3, "x": 1, "y": 0}
        r1 = Square.create(**dictionary)
        print(r1)
        expected_out = '[Square] (3) 1/0 - 3\n'
        self.assertEqual(stdout.getvalue(), expected_out)
        with self.assertRaises(TypeError):
            r1 = Square.create(1)
        with self.assertRaises(TypeError):
            r1 = Square.create('foo')
        with self.assertRaises(TypeError):
            r1 = Square.create((4, 5))
        with self.assertRaises(TypeError):
            r1 = Square.create(['foo'])
        r2 = Square.create()
        self.assertEqual(r2, None)
        with self.assertRaises(TypeError):
            r2 = Square.create('foo', 5)

    def test_load_from_file(self):
        """
        test class instance load_from_file method
        """
        PATH = './{}.json'.format(Square.__name__)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        tlist = Square.load_from_file()
        for cl in tlist:
            self.assertEqual(isinstance(cl, Square), True)
        with self.assertRaises(TypeError):
            nlist = Square.load_from_file(5)
        os.remove(PATH)

        if os.path.isfile(
                PATH) and os.access(PATH, os.R_OK) is False:
            nolist = Square.load_from_file()
            self.assertCountEqual(nolist, [])

    def test_csv(self):
        """
        test class instance csv method
        """
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file_csv([r1, r2])
        PATH = './{}.csv'.format(Square.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        content = self.write_file('{}.csv'.format(Square.__name__))
        expected_out = '1,10,2,8\n2,2,0,0\n'
        self.assertEqual(content, expected_out)

        rec1 = Square(5, 2, 8)
        rec2 = Square(2)
        Square.save_to_file_csv([rec1, rec2])
        PATH = './{}.csv'.format(Square.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.csv'.format(Square.__name__))
        expected = '3,5,2,8\n4,2,0,0\n'
        self.assertEqual(cont, expected)
        Square.save_to_file_csv(None)
        PATH = './{}.csv'.format(Square.__name__)
        self.assertEqual(os.path.isfile(
            PATH) and os.access(PATH, os.R_OK), True)
        cont = self.write_file('{}.csv'.format(Square.__name__))
        expected = ''
        self.assertEqual(cont, expected)
        with self.assertRaises(Exception):
            Square.save_to_file_csv(())
        self.assertEqual(cont, expected)
        with self.assertRaises(TypeError):
            Square.save_to_file_csv(2)
        with self.assertRaises(Exception):
            Square.save_to_file_csv('foo')
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

        r1 = Square(10, 2, 8)
        r2 = Square(2)
        list_Squares_input = [r1, r2]
        Square.save_to_file_csv(list_Squares_input)
        tlist = Square.load_from_file_csv()
        for cl in tlist:
            self.assertEqual(isinstance(cl, Square), True)
        with self.assertRaises(TypeError):
            nlist = Square.load_from_file_csv(5)
        os.remove(PATH)

        if os.path.isfile(
                PATH) and os.access(PATH, os.R_OK) is False:
            nolist = Square.load_from_file_csv()
            self.assertCountEqual(nolist, [])
