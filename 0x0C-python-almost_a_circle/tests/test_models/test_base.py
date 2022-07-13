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

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """
        test class id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        with self.assertRaises(TypeError):
            b = Base(10, 8)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)

    def test_to_json_string(self):
        """
        test class instance to_json_string method
        """
        tdict = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(Base.to_json_string([tdict]), expected)
        with self.assertRaises(TypeError):
            Base.to_json_string([tdict], [])
        tdict = {"x": 2, "size": 10, "id": 1, "y": 8}
        expected = '[{"x": 2, "size": 10, "id": 1, "y": 8}]'
        self.assertEqual(Base.to_json_string([tdict]), expected)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """
        test class instance from_json_string method
        """
        jsonstr = '[{"id": 3}, {"id": 4}]'
        tlist = Base.from_json_string(jsonstr)
        expected = [{"id": 3}, {"id": 4}]
        self.assertCountEqual(tlist, expected)
        jsonstr = ''
        tlist = Base.from_json_string(jsonstr)
        expected = []
        self.assertCountEqual(tlist, expected)
        tlist = Base.from_json_string(None)
        expected = []
        self.assertCountEqual(tlist, expected)
        with self.assertRaises(TypeError):
            Base.from_json_string()
