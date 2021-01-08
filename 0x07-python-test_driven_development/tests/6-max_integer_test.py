#!/usr/bin/python3
"""unit test for max int"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInt(unittest.TestCase):
    """testMaxInt"""
    def test_import(self):
        """import"""
        self.assertTrue(__import__("6-max_integer").max_integer)

    def test_normal(self):
        """Normal"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([15, 2, 3, 4]), 15)
        self.assertEqual(max_integer([1, 2, 13, 4]), 13)
        self.assertEqual(max_integer([1]), 1)

    def test_negative(self):
        """negative"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float(self):
        """float"""
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.69420]), -1.1)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, 4.69420]), 4.69420)
        self.assertEqual(max_integer([-1.1, -2.2, 3.3, -4.69420]), 3.3)

    def test_empty(self):
        """Nothing"""
        self.assertRaises(TypeError, max_integer, None)

    def test_NotList(self):
        self.assertRaises(TypeError, max_integer, 2)

    def test_letters(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
